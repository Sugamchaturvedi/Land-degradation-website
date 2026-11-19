# LandWatch India – Satellite Intelligence & Environmental Monitoring Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-v20%2B-green.svg)](https://nodejs.org/)
[![ISRO SAC Verified Data](https://img.shields.io/badge/Data%20Source-ISRO%20SAC%20Atlas%202021-blue.svg)](https://www.sac.gov.in/)
[![NASA GIBS](https://img.shields.io/badge/NASA%20GIBS-MODIS%20%26%20VIIRS%20NRT-red.svg)](https://worldview.earthdata.nasa.gov/)
[![Copernicus Sentinel-2](https://img.shields.io/badge/Copernicus-Sentinel--2%20MSI%2010m-blue.svg)](https://dataspace.copernicus.eu/)
[![UNCCD Alignment](https://img.shields.io/badge/UNCCD-SDG%2015.3%20LDN-emerald.svg)](https://www.unccd.int/)
[![PWA Ready](https://img.shields.io/badge/PWA-Installable-purple.svg)](./manifest.json)

A full-stack, enterprise-grade **Geospatial Environmental Intelligence & Satellite Earth Observation Platform** designed to monitor, analyze, and combat land degradation, soil erosion, and desertification across the Indian subcontinent. Calibrated against satellite-verified datasets from the **Space Applications Centre (ISRO SAC)**, **NASA GIBS**, **ESA Copernicus Sentinel-2**, **Ministry of Environment, Forest and Climate Change (MoEFCC)**, and **ICAR** research institutes.

---

## 🌍 Platform Architecture & System Overview

```
                               LANDWATCH INDIA ARCHITECTURE
                               
   +----------------------------------------------------------------------------------+
   |                              CLIENT PRESENTATION LAYER                            |
   |  • High-Res Satellite View (Esri)    • NASA GIBS Daily MODIS/VIIRS NRT           |
   |  • Leaflet.js GIS Engine             • Turf.js Advanced Geometric Measurement    |
   |  • Chart.js 4.4 Analytics            • Before-and-After Split Swipe Comparison   |
   |  • BhuMitra AI Assistant             • BhuSeva Citizen Environmental Reporting   |
   |  • Multilingual Engine (EN, HI, PA)  • Progressive Web App (PWA) Offline Cache   |
   +------------------------------------------+---------------------------------------+
                                              |
                          RESTful API / Static Fallback Hybrid
                                              |
   +------------------------------------------v---------------------------------------+
   |                               NODE.JS EXPRESS REST API                            |
   |  • /api/satellite/providers          • /api/satellite/hotspots                   |
   |  • /api/satellite/indices            • /api/reports (Citizen Reports CRUD)       |
   |  • /api/impact/calculate             • /api/compare (Multi-State Matrix)         |
   |  • /api/ai/ask (BhuMitra Engine)     • /api/auth (PBKDF2 SHA-512 Security)       |
   |  • /api/export (GeoJSON / CSV)       • /api/admin (Moderation & Telemetry)       |
   +------------------------------------------+---------------------------------------+
                                              |
   +------------------------------------------v---------------------------------------+
   |                           VERIFIED ENVIRONMENTAL DATASETS                        |
   |  • ISRO SAC Desertification & Land Degradation Atlas of India (Cycles 1, 2, 3)   |
   |  • NASA Global Imagery Browse Services (Daily Corrected Reflectance)              |
   |  • Copernicus Sentinel-2 Level-2A Multi-Spectral Surface Reflectance (NDVI/NDWI) |
   |  • ICAR-IISWC / CSSRI / CAZRI Soil Loss & Restoration Coefficients              |
   +----------------------------------------------------------------------------------+
```

---

## 🚀 Key Functional Modules

### 1. Satellite Intelligence & Live Earth Monitoring (`#satellite-view`)
- **Full-Screen Interactive Satellite Map:** Styled after Google Earth and GIS monitoring workstations with smooth pan/zoom from the national scale down to state, district, city, and farm parcels.
- **Multi-Sensor Basemap Tile Switcher:**
  1. *Esri World Imagery:* Seamless high-resolution optical satellite composites (0.3m – 15m resolution from Maxar and Airbus).
  2. *NASA GIBS Daily NRT:* Near-Real-Time true-color observations from Terra/MODIS and Suomi NPP/VIIRS sensors.
  3. *OpenTopoMap:* Topographic elevation contours and shaded relief.
  4. *OpenStreetMap:* Clear road, highway, and administrative vector layouts.
- **Dynamic Layer Overlays:**
  - *Hybrid Roads & Borders:* Political boundaries and place-name overlays.
  - *Sentinel-2 NDVI Heat-Ramp:* Multispectral vegetation health mask.
  - *ISRO SAC Degraded Boundary Mask:* Vector choropleth outlining confirmed degraded tracts.
- **Live Coordinates & Telemetry HUD:** Real-time mouse tracking displaying latitude, longitude (to 4 decimal places), current zoom level, and active satellite sensor.
- **Preset Hotspots:** One-click instant navigation to critical degradation corridors:
  - *Thar Desert Dunes (Rajasthan):* Wind deflation and shifting sand dunes.
  - *Chambal Badlands (Madhya Pradesh):* Gully erosion carving gorges up to 30m deep.
  - *Sambhar Salt Lake (Rajasthan):* Wetland contraction and severe salinization.
  - *Sundarbans Mangrove Fringe (West Bengal):* Estuarine erosion and salinity die-off.
  - *Muktsar Canal Command (Punjab):* Severe waterlogging and secondary sodicity.
- **Observation Telemetry Drawer:** Real-time metadata displaying sensor model, acquisition timestamp (UTC), cloud cover ratio (%), processing level (BOA L2A), and clear explanations of satellite orbital revisit latency (3–6 hours).
- **Split-Screen Swipe Comparison Viewer:** Draggable vertical split slider comparing **2017 Baseline** vs **2024/2025 Recent Multi-Spectral Composites** with synchronized camera panning and zooming.

### 2. Multispectral Vegetation Indices (NDVI, NDWI, NDBI)
- **Scientific Formulation:**
  $$\text{NDVI} = \frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}$$
- **Color Ramp Scale:** Deep Blue (< 0.0, water) $\rightarrow$ Earthy Brown (0.05–0.15, barren topsoil/dunes) $\rightarrow$ Light Green (0.20–0.45, rainfed crops/scrub) $\rightarrow$ Deep Forest Green (> 0.60, dense canopy).
- **Sensor Calibration:** Calibrated against Sentinel-2 Band 8 (NIR, 842nm) and Band 4 (Red, 665nm), Landsat-9 OLI, and MODIS bands.

### 3. Advanced GIS Measurement Studio (`#gis-studio-view`)
- **Turf.js Powered Spatial Geometry:**
  - *Freehand Polygon:* Click vertices to enclose custom geographical boundaries.
  - *Bounding Rectangle:* Measure rectangular agricultural plots.
  - *Circle Radius:* Distance-based radial catchment measurement.
  - *Distance Polyline:* Multi-point route and canal length measurement.
- **Live Measurement Outputs:** Computes surface area in **Hectares (Ha)**, **Square Kilometers ($\text{km}^2$)**, and **Perimeter / Distance (km and meters)**.
- **Degradation Overlap Assessment:** Automatically calculates whether the user-drawn boundary intersects with known ISRO SAC degradation risk corridors.
- **Vector Export:** Download drawn shapes as standard **GeoJSON** or **KML** files.

### 4. State vs State Comparison Studio (`#compare-view`)
- Side-by-side selection of 2 or 3 Indian States/UTs.
- Detailed comparative matrix table covering TGA, degraded area, degradation percentage, severity tier, dominant degradation process, primary drivers, and recommended restoration actions.
- Dual visual analytics:
  - *Grouped Bar Chart:* Degraded Area vs Total Area.
  - *5-Axis Radar Chart:* Vulnerability comparison across Topsoil Erosion, Aridity, Salinity, Forest Loss, and Agrarian Stress.
- One-click CSV export of comparative metrics.

### 5. Environmental Impact Assessment & Restoration Calculator (`#calculator-view`)
- Empirical biophysical calculator based on ICAR-IISWC Universal Soil Loss Equation (USLE) regional erosion factors and IPCC Tier-2 Land Use & Forestry carbon coefficients.
- Inputs: Target State, Land Area (Ha), Degradation Category, Severity, and Proposed Restoration Method.
- Computed Outputs:
  - *Topsoil Loss Prevented:* Tonnes/year.
  - *Carbon Sequestration:* $\text{tCO}_2\text{e}$/year (above- and belowground biomass and soil organic carbon).
  - *Rainwater Infiltration Boost:* $\text{m}^3$/year.
  - *Estimated Economic Preservation:* ₹ Lakhs/year.

### 6. AI Environmental Assistant – "BhuMitra AI" (`#ai-assistant-view`)
- Conversational assistant grounded in ISRO SAC 2021 Atlas data, MoEFCC reports, and ICAR agricultural guidelines.
- Quick prompt chips for common queries (Desertification in Rajasthan, Canal Salinity in Punjab, NDVI formula, Chambal ravine restoration, Satellite latency).
- Strict scientific grounding: Cites sources and states technical uncertainties when field soil tests are required.

### 7. Citizen Environmental Reporting – "BhuSeva" (`#citizen-view`)
- Public reporting portal for local communities, panchayats, and researchers.
- Pin-drop coordinate selection (auto-fills latitude, longitude, and state).
- Categories: Soil erosion, canal seepage/waterlogging, deforestation, unregulated riverbed mining, and chemical dumping.
- Photo attachment and description logging.
- Community observations feed with verification badges: `Verified`, `Under Review`, `Submitted`.
- **Admin Moderation Suite:** Integrated in the Admin Console for administrators to approve, verify, or reject submissions.

### 8. Official Environmental Report Generator (`#reports-view`)
- Formatted printable letterhead report generator with official emblems, report verification ID, generation date, and state-specific metrics.
- Print-ready CSS (`@media print`) designed for letterhead-style PDF export.
- Export raw report data as JSON.

### 9. 15-Year Historical Environmental Transition Explorer (`#historical-view`)
- Complete comparative matrix of all 36 States and UTs across:
  - *Cycle 1 (2003–05):* 94.53 Mha (28.76% of TGA).
  - *Cycle 2 (2011–13):* 96.40 Mha (29.32% of TGA).
  - *Cycle 3 (2018–19):* 97.85 Mha (29.77% of TGA).
- Visual trend indicators showing net 15-year expansion or recovery.

### 10. Multilingual Support (English, Hindi, Punjabi)
- Topbar language switcher for **English**, **हिन्दी (Hindi)**, and **ਪੰਜਾਬੀ (Punjabi)**.
- Smooth client-side translation across navigation, dashboard labels, search placeholders, and section headers.
- User preference persisted in `localStorage`.

### 11. Progressive Web App (PWA)
- Fully installable desktop/mobile PWA with [manifest.json](./manifest.json).
- [sw.js](./sw.js) Service Worker implementing Stale-While-Revalidate caching for core application assets, enabling offline review of educational resources and state profiles.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 Variables, Vanilla JavaScript (ES6+), Leaflet.js 1.9.4, Turf.js 6.5.0, Chart.js 4.4.1, FontAwesome 6 |
| **Basemap Providers** | Esri World Imagery, NASA GIBS (MODIS/VIIRS), OpenTopoMap, OpenStreetMap, Esri Reference |
| **Backend** | Node.js, Express.js 4.21, CORS |
| **Security & Auth** | PBKDF2 with SHA-512 cryptographic salting (1000 iterations), Token-based sessions |
| **Persistence** | File-backed JSON database store (`database.json`) with auto-persistence and client-side fallback |
| **PWA** | Web App Manifest, Service Worker Cache API |

---

## 📡 REST API Reference

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/health` | GET | Platform health, version, and server status. |
| `/api/states` | GET | All 36 Indian States and UTs with degradation metrics. |
| `/api/states/:id` | GET | Detailed profile for an individual state. |
| `/api/satellite/providers` | GET | Supported satellite basemaps, sensors, and licenses. |
| `/api/satellite/hotspots` | GET | Benchmark observation sites with temporal multi-cycle data. |
| `/api/satellite/indices` | GET | Multispectral index definitions (NDVI, NDWI, NDBI) and band parameters. |
| `/api/reports` | GET, POST | Fetch community reports or submit a new citizen observation. |
| `/api/reports/:id/status`| PATCH | Admin moderation (Approve, Verify, Review, Reject). |
| `/api/impact/calculate` | POST | Calculate topsoil saved, carbon sequestration, and infiltration boost. |
| `/api/compare?ids=RJ,PB` | GET | Multi-state comparative metrics matrix. |
| `/api/ai/ask` | POST | BhuMitra AI query endpoint with verified source grounding. |
| `/api/auth/login` | POST | User/Admin authentication (Default: `admin@land-intel.gov.in` / `Admin@2026`). |
| `/api/export/:type` | GET | Data export in JSON or CSV format (`states`, `quiz`, `solutions`, `news`). |

---

## 💻 Running the Platform Locally

### Option 1: Full-Stack Mode (Recommended)
This runs the Express backend on port 3000 with all REST APIs and local database persistence active:
```bash
# 1. Install dependencies
npm install

# 2. Run automated test suite
npm test

# 3. Start the server
npm start
```
Open your browser at:
```
http://localhost:3000/
```

### Option 2: VS Code Live Server Mode (Isolated Port 5505)
If you prefer viewing via the Live Server extension:
1. Open the project folder in VS Code.
2. Right-click on [index.html](./index.html) and select **"Open with Live Server"**.
3. It will open at:
   ```
   http://127.0.0.1:5505/index.html
   ```
*(Configured in `.vscode/settings.json` on port 5505 to prevent collisions with other projects on port 5500).*

---

## 🧪 Testing Results

All platform files, GeoJSON boundaries, database schemas, and REST endpoints are verified through the automated test runner:
```bash
npm test
```
**Verification Highlights:**
- `36/36` Indian States and UTs verified.
- `36` GeoJSON polygons validated.
- `55` Scientific quiz questions validated.
- `10` Restoration protocols verified.
- All Express routes verified.
- PWA `manifest.json` and `sw.js` presence confirmed.

---

## 📜 Official Data Sources & Attribution
- **ISRO SAC:** *Desertification and Land Degradation Atlas of India (2021)*, Space Applications Centre, Indian Space Research Organisation, Ahmedabad. ISBN: 978-93-87588-30-2.
- **NASA ESDIS:** Global Imagery Browse Services (GIBS) – Terra/MODIS and Suomi NPP/VIIRS.
- **ESA Copernicus:** Sentinel-2 Multi-Spectral Instrument (MSI) Level-2A surface reflectance.
- **MoEFCC:** Ministry of Environment, Forest and Climate Change, Government of India.
- **ICAR Institutes:** Central Arid Zone Research Institute (CAZRI Jodhpur), Central Soil Salinity Research Institute (CSSRI Karnal), Indian Institute of Soil and Water Conservation (IISWC Dehradun).

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
