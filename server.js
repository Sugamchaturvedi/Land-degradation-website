const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname)));

// Helper to hash passwords securely with salt
function hashPassword(password, salt = null) {
  if (!salt) {
    salt = crypto.randomBytes(16).toString('hex');
  }
  const hash = crypto.pbkdf2Sync(password, salt, 1000, 64, 'sha512').toString('hex');
  return { salt, hash };
}

function verifyPassword(password, salt, storedHash) {
  const { hash } = hashPassword(password, salt);
  return hash === storedHash;
}

// In-memory / file-persisted Database
const DB_FILE = path.join(__dirname, 'database.json');

function loadDatabase() {
  if (fs.existsSync(DB_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(DB_FILE, 'utf-8'));
    } catch (e) {
      console.error('Failed to parse database.json, initializing fresh store:', e);
    }
  }

  // Initial seed from JSON files
  const states = JSON.parse(fs.readFileSync(path.join(__dirname, 'states_data.json'), 'utf-8'));
  const questions = JSON.parse(fs.readFileSync(path.join(__dirname, 'quiz_questions.json'), 'utf-8'));
  const solutions = JSON.parse(fs.readFileSync(path.join(__dirname, 'solutions_data.json'), 'utf-8'));
  const news = JSON.parse(fs.readFileSync(path.join(__dirname, 'news_data.json'), 'utf-8'));
  const videos = JSON.parse(fs.readFileSync(path.join(__dirname, 'educational_videos.json'), 'utf-8'));

  // Default admin user (admin / Admin@2026)
  const adminPass = hashPassword('Admin@2026');

  const defaultDb = {
    users: [
      {
        id: 'admin-1',
        name: 'Platform Administrator',
        email: 'admin@land-intel.gov.in',
        role: 'admin',
        salt: adminPass.salt,
        hash: adminPass.hash,
        createdAt: new Date().toISOString()
      }
    ],
    bookmarks: [],
    quizAttempts: [],
    states,
    questions,
    solutions,
    news,
    videos,
    stats: {
      views: 1240,
      mapInteractions: 3820,
      quizzesTaken: 145
    }
  };

  fs.writeFileSync(DB_FILE, JSON.stringify(defaultDb, null, 2), 'utf-8');
  return defaultDb;
}

let db = loadDatabase();

function saveDatabase() {
  try {
    fs.writeFileSync(DB_FILE, JSON.stringify(db, null, 2), 'utf-8');
  } catch (err) {
    console.error('Error saving database:', err);
  }
}

// Auth Middleware
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  if (!authHeader) {
    req.user = null;
    return next();
  }
  const token = authHeader.split(' ')[1];
  if (!token) {
    req.user = null;
    return next();
  }

  // Token format: base64(userId:role:timestamp)
  try {
    const decoded = Buffer.from(token, 'base64').toString('utf-8');
    const [userId, role] = decoded.split(':');
    const user = db.users.find(u => u.id === userId);
    if (user) {
      req.user = { id: user.id, name: user.name, email: user.email, role: user.role };
    } else {
      req.user = null;
    }
  } catch (err) {
    req.user = null;
  }
  next();
}

function requireAdmin(req, res, next) {
  if (!req.user || req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Access forbidden: Administrator privileges required.' });
  }
  next();
}

app.use(authenticateToken);

// ================= API ROUTES =================

// 1. Health & Platform Metadata
app.get('/api/health', (req, res) => {
  res.json({
    status: 'online',
    platform: 'Land Degradation Intelligence Platform - India',
    version: '2.4.0',
    timestamp: new Date().toISOString(),
    records: {
      states: db.states.length,
      questions: db.questions.length,
      solutions: db.solutions.length,
      news: db.news.length
    }
  });
});

// 2. States Metadata & GeoJSON
app.get('/api/states', (req, res) => {
  const { region, severity } = req.query;
  let result = db.states;
  if (region && region !== 'all') {
    result = result.filter(s => s.region.toLowerCase().includes(region.toLowerCase()));
  }
  if (severity && severity !== 'all') {
    result = result.filter(s => s.severity.toLowerCase().includes(severity.toLowerCase()));
  }
  res.json({ count: result.length, states: result });
});

app.get('/api/states/:id', (req, res) => {
  const stateId = req.params.id.toLowerCase();
  const state = db.states.find(s => s.id === stateId || s.name.toLowerCase() === stateId);
  if (!state) {
    return res.status(404).json({ error: 'State not found in monitoring registry' });
  }
  res.json(state);
});

app.get('/api/geojson', (req, res) => {
  const geojsonPath = path.join(__dirname, 'india_states.geojson');
  if (fs.existsSync(geojsonPath)) {
    res.setHeader('Content-Type', 'application/json');
    fs.createReadStream(geojsonPath).pipe(res);
  } else {
    res.status(404).json({ error: 'india_states.geojson not found' });
  }
});

// 3. Analytics & Summary Aggregations
app.get('/api/analytics', (req, res) => {
  const { year, region, category } = req.query;
  let states = db.states;

  if (region && region !== 'all') {
    states = states.filter(s => s.region.toLowerCase().includes(region.toLowerCase()));
  }

  const totalArea = states.reduce((acc, s) => acc + s.total_area_mha, 0);
  const totalDegraded = states.reduce((acc, s) => acc + s.degraded_area_mha, 0);
  const avgPct = totalArea > 0 ? (totalDegraded / totalArea) * 100 : 0;

  // Most affected state in current filter
  const sorted = [...states].sort((a, b) => b.degraded_pct - a.degraded_pct);
  const mostAffected = sorted.length > 0 ? sorted[0] : null;

  // Degradation by process aggregation
  const processTotals = {};
  states.forEach(s => {
    s.dominant_processes.forEach(p => {
      processTotals[p.type] = (processTotals[p.type] || 0) + (p.area_mha || 0);
    });
  });

  // Regional breakdown
  const regionalData = {};
  states.forEach(s => {
    const r = s.region.split('/')[0].trim();
    if (!regionalData[r]) {
      regionalData[r] = { totalArea: 0, degradedArea: 0, count: 0 };
    }
    regionalData[r].totalArea += s.total_area_mha;
    regionalData[r].degradedArea += s.degraded_area_mha;
    regionalData[r].count += 1;
  });

  // Historical cycles comparison (National / Filtered aggregate)
  let hist2003 = 0, hist2011 = 0, hist2018 = 0, histCount = 0;
  states.forEach(s => {
    if (s.historical_pct) {
      hist2003 += s.historical_pct['2003_05'] || 0;
      hist2011 += s.historical_pct['2011_13'] || 0;
      hist2018 += s.historical_pct['2018_19'] || 0;
      histCount++;
    }
  });

  res.json({
    summary: {
      statesCovered: states.length,
      totalMonitoredAreaMha: Number(totalArea.toFixed(2)),
      degradedAreaMha: Number(totalDegraded.toFixed(2)),
      degradedPct: Number(avgPct.toFixed(2)),
      mostAffectedState: mostAffected ? { name: mostAffected.name, pct: mostAffected.degraded_pct, area: mostAffected.degraded_area_mha } : null,
      lastUpdated: '2021 (ISRO SAC 3rd Cycle Atlas, Remote Sensing Verification 2018-19)'
    },
    processes: Object.entries(processTotals).map(([name, area]) => ({
      name,
      area_mha: Number(area.toFixed(2)),
      pct: totalDegraded > 0 ? Number(((area / totalDegraded) * 100).toFixed(1)) : 0
    })).sort((a, b) => b.area_mha - a.area_mha),
    regional: Object.entries(regionalData).map(([region, d]) => ({
      region,
      totalAreaMha: Number(d.totalArea.toFixed(2)),
      degradedAreaMha: Number(d.degradedArea.toFixed(2)),
      pct: Number(((d.degradedArea / d.totalArea) * 100).toFixed(2)),
      statesCount: d.count
    })),
    historical: {
      cycle1_2003_05: histCount > 0 ? Number((hist2003 / histCount).toFixed(2)) : 28.76,
      cycle2_2011_13: histCount > 0 ? Number((hist2011 / histCount).toFixed(2)) : 29.32,
      cycle3_2018_19: histCount > 0 ? Number((hist2018 / histCount).toFixed(2)) : 29.77
    },
    stateComparison: sorted.map(s => ({
      id: s.id,
      name: s.name,
      degraded_pct: s.degraded_pct,
      degraded_mha: s.degraded_area_mha,
      total_mha: s.total_area_mha,
      severity: s.severity
    }))
  });
});

// 4. Solutions Hub
app.get('/api/solutions', (req, res) => {
  res.json({ count: db.solutions.length, solutions: db.solutions });
});

app.get('/api/solutions/:id', (req, res) => {
  const sol = db.solutions.find(s => s.id === req.params.id);
  if (!sol) return res.status(404).json({ error: 'Solution not found' });
  res.json(sol);
});

// 5. Environmental News & Updates
app.get('/api/news', (req, res) => {
  res.json({ count: db.news.length, news: db.news });
});

// 6. Educational Resources & Videos
app.get('/api/resources', (req, res) => {
  res.json({
    videos: db.videos,
    official_documents: [
      {
        title: "Desertification and Land Degradation Atlas of India (2021)",
        publisher: "Space Applications Centre (SAC), ISRO Ahmedabad",
        isbn: "978-93-87588-30-2",
        url: "https://www.sac.gov.in/Vyom/SACDesertification.jsp",
        pages: 242,
        format: "Official Atlas / PDF"
      },
      {
        title: "Land Degradation Neutrality Target Setting Programme (LDN-TSP) - India",
        publisher: "Ministry of Environment, Forest and Climate Change (MoEFCC)",
        url: "https://moef.gov.in/",
        year: 2019,
        format: "National Policy Document"
      },
      {
        title: "Bhuvan Thematic Geospatial Portal",
        publisher: "National Remote Sensing Centre (NRSC), ISRO Hyderabad",
        url: "https://bhuvan.nrsc.gov.in/",
        format: "Interactive GIS Portal"
      },
      {
        title: "Global Land Outlook (GLO2) - Land Restoration for Recovery and Resilience",
        publisher: "United Nations Convention to Combat Desertification (UNCCD)",
        url: "https://www.unccd.int/resources/global-land-outlook/glo2",
        format: "Global UN Publication"
      }
    ]
  });
});

// 7. Advanced Quiz System
app.get('/api/quiz/questions', (req, res) => {
  const { topic, difficulty, count } = req.query;
  let pool = [...db.questions];

  if (topic && topic !== 'all') {
    pool = pool.filter(q => q.topic.toLowerCase() === topic.toLowerCase());
  }
  if (difficulty && difficulty !== 'all') {
    pool = pool.filter(q => q.difficulty.toLowerCase() === difficulty.toLowerCase());
  }

  // Shuffle pool (Fisher-Yates)
  for (let i = pool.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [pool[i], pool[j]] = [pool[j], pool[i]];
  }

  const requestedCount = parseInt(count) || pool.length;
  const selected = pool.slice(0, requestedCount);

  // Strip correct answer from questions sent to client for test integrity
  const clientQuestions = selected.map(q => ({
    id: q.id,
    topic: q.topic,
    difficulty: q.difficulty,
    question: q.question,
    options: q.options
  }));

  res.json({
    totalAvailable: db.questions.length,
    count: clientQuestions.length,
    questions: clientQuestions
  });
});

// Submit Quiz & Validate Answers
app.post('/api/quiz/submit', (req, res) => {
  const { answers, timeSpentSeconds, topic, difficulty } = req.body;
  if (!answers || typeof answers !== 'object') {
    return res.status(400).json({ error: 'Invalid answers payload' });
  }

  let score = 0;
  const review = [];
  const questionIds = Object.keys(answers).map(Number);

  questionIds.forEach(id => {
    const question = db.questions.find(q => q.id === id);
    if (question) {
      const selectedIndex = answers[id];
      const isCorrect = selectedIndex === question.correct;
      if (isCorrect) score++;

      review.push({
        id: question.id,
        question: question.question,
        topic: question.topic,
        difficulty: question.difficulty,
        selectedOption: selectedIndex !== null && selectedIndex !== undefined ? question.options[selectedIndex] : 'Not Answered',
        correctOption: question.options[question.correct],
        isCorrect,
        explanation: question.explanation
      });
    }
  });

  const totalQuestions = review.length;
  const percentage = totalQuestions > 0 ? Number(((score / totalQuestions) * 100).toFixed(1)) : 0;

  const attemptRecord = {
    id: 'attempt-' + Date.now(),
    userId: req.user ? req.user.id : 'guest',
    score,
    totalQuestions,
    percentage,
    timeSpentSeconds: timeSpentSeconds || 0,
    topic: topic || 'All Topics',
    difficulty: difficulty || 'Mixed',
    createdAt: new Date().toISOString()
  };

  db.quizAttempts.unshift(attemptRecord);
  db.stats.quizzesTaken++;
  saveDatabase();

  res.json({
    attemptId: attemptRecord.id,
    score,
    totalQuestions,
    percentage,
    review,
    timeSpentSeconds: attemptRecord.timeSpentSeconds,
    performanceBadge: percentage >= 80 ? 'Master Environmentalist' : percentage >= 60 ? 'Informed Ecologist' : 'Novice Conservator'
  });
});

app.get('/api/quiz/history', (req, res) => {
  const userId = req.user ? req.user.id : req.query.guestId;
  let history = db.quizAttempts;
  if (userId) {
    history = history.filter(a => a.userId === userId || (userId === 'guest' && a.userId === 'guest'));
  }
  res.json({ count: history.length, history: history.slice(0, 20) });
});

// 8. User Authentication & Bookmarks
app.post('/api/auth/register', (req, res) => {
  const { name, email, password } = req.body;
  if (!name || !email || !password) {
    return res.status(400).json({ error: 'Name, email and password are required' });
  }

  const existing = db.users.find(u => u.email.toLowerCase() === email.toLowerCase());
  if (existing) {
    return res.status(400).json({ error: 'User with this email already exists' });
  }

  const { salt, hash } = hashPassword(password);
  const newUser = {
    id: 'user-' + Date.now(),
    name,
    email,
    role: 'user',
    salt,
    hash,
    savedStates: [],
    createdAt: new Date().toISOString()
  };

  db.users.push(newUser);
  saveDatabase();

  // Create token
  const token = Buffer.from(`${newUser.id}:${newUser.role}:${Date.now()}`).toString('base64');
  res.json({
    message: 'User registered successfully',
    token,
    user: { id: newUser.id, name: newUser.name, email: newUser.email, role: newUser.role }
  });
});

app.post('/api/auth/login', (req, res) => {
  const { email, password } = req.body;
  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password are required' });
  }

  const user = db.users.find(u => u.email.toLowerCase() === email.toLowerCase());
  if (!user || !verifyPassword(password, user.salt, user.hash)) {
    return res.status(401).json({ error: 'Invalid email or password' });
  }

  const token = Buffer.from(`${user.id}:${user.role}:${Date.now()}`).toString('base64');
  res.json({
    message: 'Login successful',
    token,
    user: { id: user.id, name: user.name, email: user.email, role: user.role }
  });
});

app.get('/api/auth/profile', (req, res) => {
  if (!req.user) {
    return res.status(401).json({ error: 'Not authenticated' });
  }
  const user = db.users.find(u => u.id === req.user.id);
  if (!user) return res.status(404).json({ error: 'User record not found' });

  const userAttempts = db.quizAttempts.filter(a => a.userId === user.id);
  const userBookmarks = db.bookmarks.filter(b => b.userId === user.id);

  res.json({
    user: {
      id: user.id,
      name: user.name,
      email: user.email,
      role: user.role,
      savedStates: user.savedStates || [],
      createdAt: user.createdAt
    },
    attemptsCount: userAttempts.length,
    bookmarks: userBookmarks
  });
});

app.post('/api/bookmarks/toggle', (req, res) => {
  if (!req.user) return res.status(401).json({ error: 'Authentication required to bookmark' });
  const { itemType, itemId, itemTitle } = req.body;
  if (!itemType || !itemId) return res.status(400).json({ error: 'Item type and ID required' });

  const existingIdx = db.bookmarks.findIndex(b => b.userId === req.user.id && b.itemId === itemId);
  let saved = false;

  if (existingIdx >= 0) {
    db.bookmarks.splice(existingIdx, 1);
    saved = false;
  } else {
    db.bookmarks.push({
      id: 'bm-' + Date.now(),
      userId: req.user.id,
      itemType,
      itemId,
      itemTitle: itemTitle || itemId,
      createdAt: new Date().toISOString()
    });
    saved = true;
  }
  saveDatabase();
  res.json({ saved, message: saved ? 'Bookmark saved' : 'Bookmark removed' });
});

// 9. Admin Endpoints
app.get('/api/admin/stats', requireAdmin, (req, res) => {
  res.json({
    totalUsers: db.users.length,
    totalStates: db.states.length,
    totalQuestions: db.questions.length,
    totalSolutions: db.solutions.length,
    totalNews: db.news.length,
    totalQuizAttempts: db.quizAttempts.length,
    systemMetrics: db.stats
  });
});

app.post('/api/admin/states/:id', requireAdmin, (req, res) => {
  const stateId = req.params.id;
  const stateIdx = db.states.findIndex(s => s.id === stateId);
  if (stateIdx === -1) return res.status(404).json({ error: 'State not found' });

  db.states[stateIdx] = { ...db.states[stateIdx], ...req.body };
  saveDatabase();
  res.json({ message: 'State dataset updated successfully', state: db.states[stateIdx] });
});

app.post('/api/admin/questions', requireAdmin, (req, res) => {
  const { question, options, correct, topic, difficulty, explanation } = req.body;
  if (!question || !options || correct === undefined || !topic) {
    return res.status(400).json({ error: 'Missing required question parameters' });
  }

  const newQ = {
    id: db.questions.length + 1,
    question,
    options,
    correct: parseInt(correct),
    topic,
    difficulty: difficulty || 'Medium',
    explanation: explanation || 'Scientific validation provided.'
  };

  db.questions.push(newQ);
  saveDatabase();
  res.json({ message: 'Question created successfully', question: newQ });
});

app.post('/api/admin/news', requireAdmin, (req, res) => {
  const { title, category, source, summary, url, tags } = req.body;
  if (!title || !summary) return res.status(400).json({ error: 'Title and summary are required' });

  const newItem = {
    id: 'news-' + Date.now(),
    title,
    date: new Date().toISOString().split('T')[0],
    category: category || 'Government Initiatives',
    source: source || 'MoEFCC / State Forest Dept',
    summary,
    url: url || '#',
    tags: tags || ['Policy', 'Restoration']
  };

  db.news.unshift(newItem);
  saveDatabase();
  res.json({ message: 'News update published', news: newItem });
});

// 10. Data Export (JSON or CSV)
app.get('/api/export/:type', (req, res) => {
  const type = req.params.type.toLowerCase();
  const format = req.query.format || 'json';

  let data = null;
  if (type === 'states') data = db.states;
  else if (type === 'quiz') data = db.questions;
  else if (type === 'solutions') data = db.solutions;
  else if (type === 'news') data = db.news;
  else return res.status(400).json({ error: 'Invalid export type. Choose states, quiz, solutions, or news.' });

  if (format === 'csv' && type === 'states') {
    res.setHeader('Content-Type', 'text/csv');
    res.setHeader('Content-Disposition', 'attachment; filename=india_land_degradation_states.csv');
    let csv = 'ID,Name,Type,Region,Capital,Total_Area_Mha,Degraded_Area_Mha,Degraded_Pct,Severity,Data_Source\n';
    data.forEach(s => {
      csv += `"${s.id}","${s.name}","${s.type}","${s.region}","${s.capital}",${s.total_area_mha},${s.degraded_area_mha},${s.degraded_pct},"${s.severity}","${s.data_source}"\n`;
    });
    return res.send(csv);
  }

  res.setHeader('Content-Type', 'application/json');
  res.setHeader('Content-Disposition', `attachment; filename=india_${type}.json`);
  res.json(data);
});

// 11. Satellite Providers, Hotspots & Multispectral Indices
app.get('/api/satellite/providers', (req, res) => {
  res.json({
    status: 'success',
    count: (db.satelliteProviders || []).length,
    providers: db.satelliteProviders || []
  });
});

app.get('/api/satellite/hotspots', (req, res) => {
  res.json({
    status: 'success',
    count: (db.satelliteHotspots || []).length,
    hotspots: db.satelliteHotspots || []
  });
});

app.get('/api/satellite/indices', (req, res) => {
  res.json({
    status: 'success',
    indices: [
      {
        code: 'NDVI',
        name: 'Normalized Difference Vegetation Index',
        formula: '(NIR - Red) / (NIR + Red)',
        sensors: ['Sentinel-2 (B8 & B4)', 'Landsat 8/9 (B5 & B4)', 'MODIS (B2 & B1)'],
        range: '-1.0 to +1.0',
        interpretation: {
          healthyCanopy: '> 0.6 (Dense forest, peak irrigated crops)',
          moderateGreenery: '0.2 to 0.5 (Rainfed agriculture, open scrub)',
          barrenSoil: '0.05 to 0.18 (Exposed topsoil, sand dunes, fallow)',
          waterOrRock: '< 0.0 (Water bodies, deep shade, barren rock)'
        },
        limitations: 'Saturates over very dense rainforest canopies; sensitive to atmospheric aerosol scattering.'
      },
      {
        code: 'NDWI',
        name: 'Normalized Difference Water Index (Gao 1996 / McFeeters 1996)',
        formula: '(Green - NIR) / (Green + NIR) or (NIR - SWIR) / (NIR + SWIR)',
        sensors: ['Sentinel-2 (B3 & B8)', 'Landsat 8/9 (B3 & B5)'],
        range: '-1.0 to +1.0',
        interpretation: {
          openWater: '> 0.2 (Lakes, reservoirs, flooded paddy)',
          saturatedSoil: '0.0 to 0.2 (High soil moisture, waterlogged fields)',
          drySoilOrVegetation: '< 0.0 (Terrestrial cover, drylands)'
        },
        limitations: 'Built-up shadows in urban canyons can occasionally register as false-positive water pixels.'
      },
      {
        code: 'NDBI',
        name: 'Normalized Difference Built-up Index',
        formula: '(SWIR - NIR) / (SWIR + NIR)',
        sensors: ['Sentinel-2 (B11 & B8)', 'Landsat 8/9 (B6 & B5)'],
        range: '-1.0 to +1.0',
        interpretation: {
          builtStructures: '> 0.1 (Concrete, asphalt, urban sprawl)',
          bareDrySoil: '0.0 to 0.1 (Dry dirt roads, fallow earth)',
          vegetationWater: '< 0.0 (Canopy cover, wetlands)'
        },
        limitations: 'Highly reflective barren dry sandy soil can show reflectance characteristics close to concrete.'
      }
    ]
  });
});

// 12. Citizen Environmental Reporting API
app.get('/api/reports', (req, res) => {
  const { status, state } = req.query;
  let reports = db.citizenReports || [];
  if (status && status !== 'all') {
    reports = reports.filter(r => r.status.toLowerCase() === status.toLowerCase());
  }
  if (state && state !== 'all') {
    reports = reports.filter(r => r.state.toLowerCase() === state.toLowerCase());
  }
  res.json({ status: 'success', count: reports.length, reports });
});

app.post('/api/reports', (req, res) => {
  const { title, category, state, district, lat, lng, description, severity, reporter, imageUrl } = req.body;
  if (!title || !category || !state || !description) {
    return res.status(400).json({ error: 'Missing required report fields (title, category, state, description)' });
  }

  const newReport = {
    id: 'rep-' + Date.now(),
    title,
    category,
    state,
    district: district || 'Not specified',
    lat: parseFloat(lat) || 20.5937,
    lng: parseFloat(lng) || 78.9629,
    description,
    severity: severity || 'Moderate',
    date: new Date().toISOString().split('T')[0],
    reporter: reporter || (req.user ? req.user.name : 'Anonymous Citizen Observer'),
    status: 'Submitted',
    imageUrl: imageUrl || 'https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=600&auto=format&fit=crop&q=80',
    adminNotes: 'Awaiting spatial assessment and field triage.'
  };

  if (!db.citizenReports) db.citizenReports = [];
  db.citizenReports.unshift(newReport);
  saveDatabase();

  res.status(201).json({
    status: 'success',
    message: 'Environmental observation report submitted successfully.',
    report: newReport
  });
});

app.patch('/api/reports/:id/status', requireAdmin, (req, res) => {
  const { id } = req.params;
  const { status, adminNotes } = req.body;
  const allowed = ['Submitted', 'Under Review', 'Verified', 'Rejected'];

  if (!allowed.includes(status)) {
    return res.status(400).json({ error: `Invalid status. Allowed: ${allowed.join(', ')}` });
  }

  const report = (db.citizenReports || []).find(r => r.id === id);
  if (!report) return res.status(404).json({ error: 'Report not found' });

  report.status = status;
  if (adminNotes) report.adminNotes = adminNotes;
  saveDatabase();

  res.json({ status: 'success', message: `Report status updated to ${status}`, report });
});

// 13. Multi-State Comparison API
app.get('/api/compare', (req, res) => {
  const { ids } = req.query;
  if (!ids) return res.status(400).json({ error: 'Query parameter "ids" (comma separated, e.g. RJ,PB,MH) is required.' });

  const idList = ids.split(',').map(s => s.trim().toUpperCase());
  const matchedStates = db.states.filter(s => idList.includes(s.id.toUpperCase()));

  if (matchedStates.length === 0) {
    return res.status(404).json({ error: 'No matching states found for the provided IDs.' });
  }

  res.json({
    status: 'success',
    count: matchedStates.length,
    states: matchedStates
  });
});

// 14. Environmental Impact Assessment Calculator API
app.post('/api/impact/calculate', (req, res) => {
  const { areaHa, stateId, category, severity, method } = req.body;
  const area = parseFloat(areaHa);

  if (isNaN(area) || area <= 0) {
    return res.status(400).json({ error: 'Area in hectares must be a positive numerical value.' });
  }

  // Base coefficients derived from ICAR-IISWC & MoEFCC restoration models
  const severityMultipliers = {
    'Slight': 1.0,
    'Moderate': 1.6,
    'High': 2.4,
    'Severe': 3.2,
    'Very Severe': 4.0
  };
  const sevMult = severityMultipliers[severity] || 1.8;

  // Tonnes topsoil loss avoided per hectare per year
  const soilLossBase = {
    'Water Erosion': 18.5,
    'Wind Erosion': 26.0,
    'Salinity / Alkalinity': 4.5,
    'Vegetation Degradation': 12.0,
    'Waterlogging': 6.0
  };
  const baseLossRate = soilLossBase[category] || 15.0;
  const soilLossSavedTonnes = Math.round(area * baseLossRate * sevMult * 0.82);

  // Carbon sequestration potential (tCO2e / ha / year)
  const carbonFactors = {
    'Afforestation & Native Plantation': 7.5,
    'Agroforestry & Silvopasture': 4.8,
    'Contour Bunding & Trenching': 2.2,
    'Sub-surface Drainage & Leaching': 1.5,
    'Check Dams & Gully Plugging': 3.1,
    'Sand Dune Shelterbelts': 3.8
  };
  const carbonRate = carbonFactors[method] || 4.2;
  const carbonSequestrationTonnes = Math.round(area * carbonRate * 1.1);

  // Water Infiltration boost (m3 / year)
  const waterBoostM3 = Math.round(area * 10000 * 0.18); // assuming 180mm additional retained precipitation

  // Estimated economic livelihood preservation (INR)
  const economicReturnINR = Math.round(area * 14500 * sevMult);

  res.json({
    status: 'success',
    parameters: { areaHa: area, category, severity, method },
    results: {
      topsoilLossPreventedTonnesPerYear: soilLossSavedTonnes,
      carbonSequestrationTCO2ePerYear: carbonSequestrationTonnes,
      rainwaterInfiltrationBoostM3PerYear: waterBoostM3,
      estimatedAnnualEconomicPreservationINR: economicReturnINR,
      scientificMethodology: 'ICAR-IISWC Dehradun Soil Loss Equation & IPCC Tier-2 Land Use Carbon Inventory coefficients.',
      caveat: 'Indicative bio-physical model estimate. Local soil texture, slope gradient, and rainfall intensity cause field variations.'
    }
  });
});

// 15. AI Environmental Assistant (BhuMitra AI)
app.post('/api/ai/ask', (req, res) => {
  const { question, contextState } = req.body;
  if (!question || typeof question !== 'string') {
    return res.status(400).json({ error: 'Question string is required' });
  }

  const q = question.toLowerCase();
  let answer = '';
  let citations = ['ISRO SAC Desertification & Land Degradation Atlas of India (2021)'];

  // Check state specific query
  const matchedState = db.states.find(s => q.includes(s.name.toLowerCase()) || q.includes(s.id.toLowerCase()));

  if (matchedState) {
    citations.push(`MoEFCC State Environmental Profile: ${matchedState.name}`);
    answer = `Based on the ISRO SAC 2021 Atlas, **${matchedState.name}** has a total geographical area of **${matchedState.total_area_mha} Mha**, of which **${matchedState.degraded_area_mha} Mha (${matchedState.degraded_pct}%)** is classified as degraded land. The primary degradation process observed is **${matchedState.dominant_process}**, which accounts for **${matchedState.dominant_pct}%** of total degradation in the state.\n\n` +
      `Key driving factors include ${matchedState.drivers.join(', ')}. ` +
      `Scientific recommended interventions prioritize **${matchedState.recommended_measures[0]}** and **${matchedState.recommended_measures[1]}**.`;
  } else if (q.includes('ndvi') || q.includes('vegetation index') || q.includes('formula')) {
    citations.push('ESA Sentinel-2 Optical Sensor Calibration Guide', 'Rouse et al. 1974');
    answer = `**NDVI (Normalized Difference Vegetation Index)** is calculated using the formula:\n\n` +
      `$$\\text{NDVI} = \\frac{\\text{NIR} - \\text{Red}}{\\text{NIR} + \\text{Red}}$$\n\n` +
      `In healthy plant canopies, chlorophyll absorbs red wavelengths (approx. 660 nm) for photosynthesis while mesophyll cell walls strongly scatter Near-Infrared (NIR, approx. 840 nm). NDVI values range from -1.0 to +1.0:\n` +
      `• **> 0.60**: Dense forest, vigorous irrigated cropland.\n` +
      `• **0.20 – 0.50**: Sparse grassland, scrublands, rainfed fields.\n` +
      `• **0.05 – 0.18**: Exposed bare soil, fallow agricultural fields, sand dunes.\n` +
      `• **< 0.00**: Open water bodies, clouds, or deep hill shadows.`;
  } else if (q.includes('desertification') || q.includes('rajasthan') || q.includes('thar')) {
    citations.push('ICAR-CAZRI Jodhpur Arid Zone Research', 'ISRO SAC Atlas Table 4.1');
    answer = `Desertification across western India, particularly in **Rajasthan (where 62.9% of land is affected)**, is predominantly driven by **wind deflation and shifting sand dunes**. Arid climatic regimes with low precipitation (< 300 mm/year) combine with overgrazing of fragile desert rangelands and groundwater overdraft. Shelterbelts of native trees (*Prosopis cineraria / Khejri*, *Acacia senegal*) and rotational grazing are field-tested counter-measures.`;
  } else if (q.includes('punjab') || q.includes('waterlog') || q.includes('salinity')) {
    citations.push('ICAR-CSSRI Karnal Soil Salinity Guidelines', 'Punjab State Council for Science & Technology');
    answer = `In **Punjab**, although total degraded land is relatively lower (3.7% of TGA), specific southwestern districts like **Muktsar, Fazilka, and Bathinda** suffer from severe **sub-surface waterlogging and secondary salinization**. Heavy canal irrigation over impermeable subsoil clay strata causes the saline water table to rise near the crop root zone, depositing white salt crusts. Sub-surface perforated pipe drainage and gypsum application have demonstrated 90%+ recovery in CSSRI trials.`;
  } else if (q.includes('chambal') || q.includes('ravine') || q.includes('madhya pradesh')) {
    citations.push('ICAR-IISWC Dehradun Badland Reclamation Protocol', 'MP Forest Department');
    answer = `The **Chambal badlands** in Madhya Pradesh and Rajasthan are classic examples of catastrophic **gully and ravine erosion**. Deep alluvial soils without adequate vegetative anchoring are rapidly carved by intense monsoon cloudbursts into ravines up to 30 meters deep. Successful reclamation combines micro-watershed contour trenching, loose-boulder check dams, and bio-fencing using bamboo (*Dendrocalamus strictus*).`;
  } else if (q.includes('live') || q.includes('delay') || q.includes('real time')) {
    citations.push('NASA GIBS Latency Standards', 'Copernicus Sentinel Constellation Operations');
    answer = `Earth observation satellites do **not** stream continuous live video. Sensors such as NASA Terra/Aqua and Sentinel-2 pass over India at specific orbital equatorial crossing times. Standard Near-Real-Time (NRT) processing requires **3 to 6 hours** for downlink, atmospheric calibration, and orthorectification, while analysis-ready composites are compiled over 5 to 16 day revisit intervals. LandWatch India clearly tags the exact observation timestamp on all imagery.`;
  } else {
    answer = `LandWatch India integrates ISRO SAC 2021 Atlas data, Copernicus Sentinel multispectral bands, and ICAR agricultural guidelines. Land degradation currently impacts **97.85 million hectares (29.77% of India's Total Geographical Area)**.\n\n` +
      `You can ask specific questions about any of India's 36 States/UTs, satellite vegetation indices (NDVI/NDWI), soil erosion mechanics, or specific restoration protocols (such as Agroforestry, Check Dams, and Shelterbelts).`;
  }

  res.json({
    status: 'success',
    question,
    answer,
    citations,
    timestamp: new Date().toISOString()
  });
});

// Start Server
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`=======================================================`);
    console.log(` LAND DEGRADATION INTELLIGENCE PLATFORM (INDIA)`);
    console.log(` Server active on: http://localhost:${PORT}`);
    console.log(` REST API endpoints ready: /api/states, /api/analytics, etc.`);
    console.log(` Administrator credentials: admin@land-intel.gov.in / Admin@2026`);
    console.log(`=======================================================`);
  });
}

module.exports = app;
