import json

quiz_questions = [
    # Topic 1: Soil Erosion & Physical Degradation
    {
        "id": 1,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Easy",
        "question": "Which natural agent is the primary driver of soil erosion across mainland India?",
        "options": ["Running water (water erosion)", "Wind deflection", "Glacial movement", "Volcanic activity"],
        "correct": 0,
        "explanation": "According to the ISRO Desertification and Land Degradation Atlas 2021, water erosion is the single largest contributor, affecting approximately 11.01% of India's total geographical area (36.19 million hectares)."
    },
    {
        "id": 2,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Medium",
        "question": "Which stage of water erosion removes a uniform, thin layer of topsoil often unnoticed by farmers?",
        "options": ["Splash erosion", "Sheet erosion", "Rill erosion", "Gully erosion"],
        "correct": 1,
        "explanation": "Sheet erosion involves the uniform removal of a thin layer of topsoil across an entire field by surface runoff. Because it occurs gradually without deep cuts, it is often called the 'silent thief' of soil fertility."
    },
    {
        "id": 3,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Hard",
        "question": "What is the critical threshold of topsoil loss above which natural soil formation cannot keep pace in tropical conditions?",
        "options": ["0.5 to 1.0 tons/ha/year", "4.0 to 11.2 tons/ha/year", "25 to 40 tons/ha/year", "80 to 120 tons/ha/year"],
        "correct": 1,
        "explanation": "Soil loss tolerance (T-value), defined by ICAR-IISWC Dehradun, ranges between 4.0 and 11.2 tons/ha/year depending on soil depth and profile. Current erosion in degraded Indian catchments often exceeds 20-40 tons/ha/year."
    },
    {
        "id": 4,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Medium",
        "question": "Which famous geographical region in Central India is characterized by severe network gully erosion forming extensive badlands?",
        "options": ["Chambal River Basin", "Malwa Plateau", "Konkan Coastal Plain", "Brahmaputra Valley"],
        "correct": 0,
        "explanation": "The Chambal river basin in Madhya Pradesh and Rajasthan has over 400,000 hectares of deep ravines (gullies exceeding 15–20 meters depth) carved into deep alluvial deposits."
    },
    {
        "id": 5,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Easy",
        "question": "What agricultural practice on hill slopes aligns ploughing along constant elevation contours to slow runoff?",
        "options": ["Contour plowing", "Slash and burn", "Deep furrow subsoiling", "Flood irrigation"],
        "correct": 0,
        "explanation": "Contour plowing forms miniature ridges and furrows across the slope at equal elevation, functioning as mini-dams that capture rainfall and prevent water runoff from gathering erosive velocity."
    },
    {
        "id": 6,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Medium",
        "question": "Which deep-rooted perennial grass is internationally endorsed for biological slope stabilization and erosion control?",
        "options": ["Bermuda grass", "Vetiver grass (Chrysopogon zizanioides)", "Elephant grass", "Lemon grass"],
        "correct": 1,
        "explanation": "Vetiver grass forms an underground root network descending 2 to 4 meters with high tensile strength, acting as a living soil nail barrier against landslides and sheet runoff."
    },
    {
        "id": 7,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Hard",
        "question": "In the Universal Soil Loss Equation (USLE: A = R * K * L * S * C * P), what does the 'K' factor represent?",
        "options": ["Rainfall erosivity factor", "Soil erodibility factor", "Slope steepness factor", "Conservation practice factor"],
        "correct": 1,
        "explanation": "In USLE, 'K' designates soil erodibility: the inherent susceptibility of a specific soil type to detachment and transport based on texture, organic matter content, structure, and permeability."
    },
    {
        "id": 8,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Easy",
        "question": "What is the physical detachment and skipping movement of sand grains driven by wind near the ground called?",
        "options": ["Saltation", "Suspension", "Surface creep", "Abrasion"],
        "correct": 0,
        "explanation": "Saltation accounts for 50% to 70% of total wind erosion, where sand particles (0.1 to 0.5 mm) bounce along the ground surface dislodging other particles upon impact."
    },
    {
        "id": 9,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Medium",
        "question": "Which Indian state experiences the highest absolute volume of wind erosion?",
        "options": ["Punjab", "Rajasthan", "Madhya Pradesh", "Karnataka"],
        "correct": 1,
        "explanation": "Rajasthan experiences over 15.20 million hectares of wind-degraded land, primarily across western arid districts such as Jaisalmer, Bikaner, and Barmer."
    },
    {
        "id": 10,
        "topic": "Soil Erosion & Mechanics",
        "difficulty": "Hard",
        "question": "What structure is built across a gully channel to reduce runoff velocity and trap sediment?",
        "options": ["Check dam (loose boulder or gabion)", "Percolation well", "Sub-surface tile drain", "Dike levee"],
        "correct": 0,
        "explanation": "Check dams are grade-stabilization structures placed across active gullies that reduce the hydraulic gradient, dissipate kinetic energy, and accumulate fertile silt behind them."
    },

    # Topic 2: Desertification & Arid Land Dynamics
    {
        "id": 11,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Easy",
        "question": "According to the UNCCD definition, desertification refers to land degradation occurring specifically in which bioclimatic zones?",
        "options": ["Tropical rainforests only", "Arid, semi-arid, and dry sub-humid areas", "Arctic tundra and polar zones", "Coastal marine wetlands"],
        "correct": 1,
        "explanation": "The United Nations Convention to Combat Desertification (UNCCD) defines desertification strictly as land degradation in arid, semi-arid, and dry sub-humid areas resulting from various factors, including climatic variations and human activities."
    },
    {
        "id": 12,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Medium",
        "question": "What indigenous multi-purpose tree species is known as the 'Lifeline of the Thar Desert' in Rajasthan?",
        "options": ["Azadirachta indica (Neem)", "Prosopis cineraria (Khejri)", "Eucalyptus globulus", "Tectona grandis (Teak)"],
        "correct": 1,
        "explanation": "Prosopis cineraria (Khejri) fixes atmospheric nitrogen, provides nutritious green fodder (Loong) during extreme drought, stabilizes sand dunes, and allows crops to grow vigorously right up to its trunk."
    },
    {
        "id": 13,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Hard",
        "question": "What is the approximate Aridity Index (P/PET: Precipitation divided by Potential Evapotranspiration) range defining semi-arid zones?",
        "options": ["< 0.05", "0.05 to 0.20", "0.20 to 0.50", "0.65 to 1.00"],
        "correct": 2,
        "explanation": "Under UNEP and UNCCD criteria: Hyper-arid is < 0.05; Arid is 0.05 to 0.20; Semi-arid is 0.20 to 0.50; Dry sub-humid is 0.50 to 0.65."
    },
    {
        "id": 14,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Medium",
        "question": "The proposed 'Great Green Wall of India' aims to create an ecological green belt along which ancient mountain system?",
        "options": ["Western Ghats", "Aravalli Range", "Vindhya Range", "Himalayan Foothills"],
        "correct": 1,
        "explanation": "The Green Wall of India is envisioned as a 1,400 km long and 5 km wide green belt running along the Aravalli range from Porbandar (Gujarat) to Panipat (Haryana) to act as a barrier against eastward desert expansion."
    },
    {
        "id": 15,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Easy",
        "question": "Which Indian research institute headquartered in Jodhpur conducts premier scientific research on arid zone agriculture and desert control?",
        "options": ["ICAR-CAZRI (Central Arid Zone Research Institute)", "ICAR-CRIDA", "ICAR-CSSRI", "FRI Dehradun"],
        "correct": 0,
        "explanation": "The Central Arid Zone Research Institute (CAZRI) in Jodhpur, established in 1959 under ICAR, leads research on sand dune stabilization, arid horticulture, and renewable energy in desert environments."
    },
    {
        "id": 16,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Medium",
        "question": "What cold desert union territory of India experiences high-altitude desertification due to the Himalayan rain-shadow effect?",
        "options": ["Ladakh", "Sikkim", "Uttarakhand", "Puducherry"],
        "correct": 0,
        "explanation": "Ladakh is a high-altitude cold desert receiving less than 100 mm of annual rainfall, where extreme freeze-thaw cycles, wind erosion, and bare soils create unique desertification challenges."
    },
    {
        "id": 17,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Hard",
        "question": "What innovative artificial water-harvesting structure was developed in Ladakh to store winter stream water for springtime agricultural irrigation?",
        "options": ["Khadin system", "Ice Stupa (Artificial Glacier)", "Johad", "Ahar-Pyne"],
        "correct": 1,
        "explanation": "Invented by Ladakhi engineer Sonam Wangchuk, Ice Stupas freeze winter runoff into vertical cone-shaped ice towers that melt slowly during April and May when farmers need critical water for spring sowing."
    },
    {
        "id": 18,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Medium",
        "question": "What traditional runoff harvesting system in Jaisalmer utilizes an earthen bund across a gentle slope to cultivate hyper-arid soils?",
        "options": ["Khadin (or Dhora)", "Kund / Tanka", "Bawari", "Surangam"],
        "correct": 0,
        "explanation": "Developed by the Paliwal Brahmins in the 15th century, a Khadin collects flash flood runoff behind an embankment; the soil absorbs the moisture and is cultivated for winter crops (wheat/gram) without supplementary irrigation."
    },
    {
        "id": 19,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Easy",
        "question": "How does excessive livestock grazing accelerate desertification?",
        "options": ["Removes protective vegetation cover and compacts topsoil with hooves", "Increases soil nitrogen content to toxic levels", "Stops rainfall from condensing in clouds", "Attracts destructive burrowing termites"],
        "correct": 0,
        "explanation": "Overgrazing strips perennial grass cover that protects soil from wind deflation, while trampling by animal hooves crushes soil aggregates into fine dust, rendering it highly vulnerable to erosion."
    },
    {
        "id": 20,
        "topic": "Desertification & Arid Lands",
        "difficulty": "Hard",
        "question": "In sand dune stabilization protocols, what is 'checkerboard' micro-windbreak mulching?",
        "options": ["Planting trees in diamond shapes", "Erecting grid-like brushwood or straw barriers in 2-5m squares across dune crests", "Spraying petroleum emulsions across the dune", "Digging circular pits around shrubs"],
        "correct": 1,
        "explanation": "Checkerboard mulching embeds dried brushwood, Crotalaria, or straw in 2x2 to 5x5 meter grids oriented against prevailing winds. This reduces boundary layer wind velocity, halting sand movement until planted vegetation establishes."
    },

    # Topic 3: Soil Salinity, Sodicity & Waterlogging
    {
        "id": 21,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Easy",
        "question": "What visual indicator typically appears on the surface of saline soils during dry periods?",
        "options": ["A white crystalline salt crust", "A glossy dark green moss layer", "A bright red rust deposit", "A deep black tarry sheen"],
        "correct": 0,
        "explanation": "Saline soils (Solonchaks) exhibit a distinct white efflorescence of soluble chloride and sulfate salts brought to the surface by capillary water rise and left behind after surface evaporation."
    },
    {
        "id": 22,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Medium",
        "question": "Which chemical amendment is standardly applied to reclaim sodic (alkali) soils characterized by excess exchangeable sodium?",
        "options": ["Urea", "Agricultural Gypsum (Calcium Sulfate Dihydrate)", "Sodium chloride", "Muriate of Potash"],
        "correct": 1,
        "explanation": "Gypsum (CaSO4.2H2O) supplies soluble Calcium (Ca2+) ions that displace toxic Exchangeable Sodium (Na+) from soil clay colloids. The displaced sodium sulfate is then leached downward with fresh irrigation water."
    },
    {
        "id": 23,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Hard",
        "question": "What is the defining chemical threshold for a soil to be classified as Sodic (Alkali)?",
        "options": ["Electrical Conductivity (EC) > 10 dS/m", "Exchangeable Sodium Percentage (ESP) >= 15% and pH > 8.5", "Organic Carbon < 0.1%", "Available Nitrogen < 100 kg/ha"],
        "correct": 1,
        "explanation": "By definition (USDA / CSSRI Karnal standards), sodic soils possess an ESP >= 15%, Electrical Conductivity (ECe) < 4.0 dS/m, and a saturated paste pH typically exceeding 8.5, which causes clay dispersion and loss of pore structure."
    },
    {
        "id": 24,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Medium",
        "question": "Why does over-irrigation in canal command areas (such as the Indira Gandhi Canal or Sharda Sahayak) induce secondary salinization?",
        "options": ["Canal water is pure brine", "It causes groundwater tables to rise, bringing dissolved mineral salts into the crop root zone", "It kills beneficial earthworms immediately", "It dissolves all soil phosphorus into gas"],
        "correct": 1,
        "explanation": "Unlined canals and excessive flood irrigation cause the underground water table to rise over decades. Once the saline water table reaches within 1 to 2 meters of the surface, capillary action wicks moisture upward where evaporation leaves salts behind."
    },
    {
        "id": 25,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Easy",
        "question": "Which premier ICAR institute located in Karnal, Haryana specializes in soil salinity research and technology?",
        "options": ["ICAR-CSSRI (Central Soil Salinity Research Institute)", "ICAR-IARI", "ICAR-CRIDA", "ICAR-IIHR"],
        "correct": 0,
        "explanation": "The Central Soil Salinity Research Institute (CSSRI) in Karnal, established in 1969, has developed flagship technologies including sub-surface drainage, gypsum beds, and salt-tolerant crop varieties (CSR series)."
    },
    {
        "id": 26,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Medium",
        "question": "Which of the following is a salt-tolerant rice variety developed by ICAR-CSSRI for saline and sodic lands in India?",
        "options": ["CSR 30", "Sonalika", "IR 8", "Pusa Basmati 1121"],
        "correct": 0,
        "explanation": "CSR 30 (along with CSR 27 and CSR 36) is an elite salt-tolerant Basmati rice variety that produces high yields even in soils with pH up to 9.5 and ECe up to 7 dS/m."
    },
    {
        "id": 27,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Hard",
        "question": "What is Sub-Surface Drainage (SSD) technology used for in waterlogged saline agricultural lands?",
        "options": ["Spraying water from high-pressure nozzles", "Laying perforated corrugated PVC pipes wrapped in synthetic geotextile below the root zone to evacuate saline water", "Digging open borewells every 10 meters", "Flooding fields with acidic river water"],
        "correct": 1,
        "explanation": "Sub-surface drainage places perforated corrugated drainage pipes at 1.2 to 1.75 meters depth. When the water table rises above the pipes, excess saline water enters through perforations and flows via gravity or sumps into disposal drains, permanently de-salinizing the root zone."
    },
    {
        "id": 28,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Easy",
        "question": "What green manuring crop is widely grown and ploughed into alkaline/sodic soils to release organic acids and assist gypsum reclamation?",
        "options": ["Sesbania aculeata (Dhaincha)", "Wheat", "Sugarcane", "Eucalyptus"],
        "correct": 0,
        "explanation": "Dhaincha (Sesbania aculeata) tolerates sodic conditions and high pH; upon incorporation into the soil, its decomposition releases carbon dioxide and organic acids that lower pH and solubilize native calcium carbonate."
    },
    {
        "id": 29,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Medium",
        "question": "In which coastal delta of West Bengal has soil salinity spiked drastically due to storm surges from cyclones such as Amphan and Yaas?",
        "options": ["Sundarbans", "Kutch Delta", "Cauvery Delta", "Mahanadi Delta"],
        "correct": 0,
        "explanation": "Cyclones breach coastal earthen embankments in the Sundarbans, submerging thousands of hectares of fertile multi-crop paddy lands under high-salinity seawater that takes years to leach out."
    },
    {
        "id": 30,
        "topic": "Salinity, Sodicity & Waterlogging",
        "difficulty": "Hard",
        "question": "What physiological condition occurs in plants growing in highly saline soils despite water being physically present?",
        "options": ["Etiolation", "Physiological drought (osmotic stress)", "Guttation overload", "Chlorosis necrosis hybrid"],
        "correct": 1,
        "explanation": "High salt concentration in the soil solution lowers the osmotic potential below that of plant root cells, preventing roots from absorbing water and causing the plant to suffer dehydration ('physiological drought')."
    },

    # Topic 4: Deforestation, Mining & Vegetation Degradation
    {
        "id": 31,
        "topic": "Deforestation & Mining",
        "difficulty": "Easy",
        "question": "What traditional agricultural practice in northeastern Indian states involves clearing and burning forest patches on hill slopes?",
        "options": ["Jhum (Shifting Cultivation)", "Terrace cultivation", "Aquaponics", "Hydroponics"],
        "correct": 0,
        "explanation": "Jhum cultivation (slash-and-burn) involves felling trees, burning biomass for ash fertility, cultivating for 1-2 seasons, and leaving the land fallow. Reduced fallow cycles now cause severe soil loss."
    },
    {
        "id": 32,
        "topic": "Deforestation & Mining",
        "difficulty": "Medium",
        "question": "What severe environmental degradation phenomenon occurs when unscientific rat-hole coal mining in Meghalaya exposes pyritic rocks to air and water?",
        "options": ["Thermal inversion", "Acid Mine Drainage (AMD)", "Ozone depletion", "Eutrophication"],
        "correct": 1,
        "explanation": "Oxidation of pyrite (FeS2) in exposed coal seams produces sulfuric acid, leading to Acid Mine Drainage (AMD). AMD leaches toxic heavy metals and turns streams (such as the Lukha river) intensely acidic (pH 2.5–3.5), killing aquatic life and sterilizing soils."
    },
    {
        "id": 33,
        "topic": "Deforestation & Mining",
        "difficulty": "Hard",
        "question": "Which Indian state has the highest percentage of its land area classified as degraded, primarily driven by open-cast mining and vegetation loss?",
        "options": ["Jharkhand", "Punjab", "Kerala", "Sikkim"],
        "correct": 0,
        "explanation": "According to the ISRO SAC Atlas 2021, Jharkhand has approximately 69.01% of its geographical area degraded, driven by vegetation degradation, sheet erosion on the Chota Nagpur Plateau, and extensive mining overburden dumps."
    },
    {
        "id": 34,
        "topic": "Deforestation & Mining",
        "difficulty": "Easy",
        "question": "How does forest canopy cover directly mitigate soil erosion during intense tropical rainfall?",
        "options": ["Absorbs raindrops directly into wood", "Intercepts falling raindrops, dissipating their kinetic energy before reaching topsoil", "Releases chemical anti-erosion vapors into the atmosphere", "Freezes topsoil moisture"],
        "correct": 1,
        "explanation": "The multi-tiered canopy of forests intercepts high-velocity raindrops and reduces their terminal velocity. Leaf litter on the forest floor acts as a sponge, allowing rainwater to gently infiltrate rather than create surface runoff."
    },
    {
        "id": 35,
        "topic": "Deforestation & Mining",
        "difficulty": "Medium",
        "question": "What statutory fund was created under Indian law to receive compensatory payments from developers diverting forest land for non-forest purposes?",
        "options": ["CAMPA (Compensatory Afforestation Fund Management and Planning Authority)", "Green Climate Fund", "Swachh Bharat Kosh", "Clean Energy Cess"],
        "correct": 0,
        "explanation": "CAMPA manages national and state compensatory afforestation funds collected under the Forest (Conservation) Act, earmarked specifically for artificial regeneration, silvicultural operations, and catchment area treatment."
    },
    {
        "id": 36,
        "topic": "Deforestation & Mining",
        "difficulty": "Hard",
        "question": "What biological remediation technique uses hyper-accumulator plants to stabilize and detoxify heavy-metal-laden mining overburden?",
        "options": ["Bioreactor distillation", "Phytoremediation", "Electrodialysis reversal", "Thermal desorption"],
        "correct": 1,
        "explanation": "Phytoremediation employs specialized deep-rooted plants, grasses, and mycorrhizal fungi to extract, immobilize, or volatilize heavy metal contaminants (such as lead, arsenic, chromium) from degraded mine tailings."
    },
    {
        "id": 37,
        "topic": "Deforestation & Mining",
        "difficulty": "Easy",
        "question": "What term describes the complete covering of natural soil by impervious human infrastructure such as concrete and asphalt?",
        "options": ["Soil sealing", "Soil calcification", "Soil aeration", "Soil humification"],
        "correct": 0,
        "explanation": "Soil sealing permanently destroys ecological functions by capping living soil beneath impermeable concrete, bitumen, and buildings, preventing water infiltration and soil gas exchange in expanding urban agglomerations."
    },
    {
        "id": 38,
        "topic": "Deforestation & Mining",
        "difficulty": "Medium",
        "question": "Which invasive alien shrub species originally introduced as live fencing has aggressively overtaken vast semi-arid pastures and degraded native Banni grasslands in Gujarat?",
        "options": ["Prosopis juliflora (Vilayati Kikar)", "Parthenium hysterophorus", "Lantana camara", "Water hyacinth"],
        "correct": 0,
        "explanation": "Prosopis juliflora has colonized millions of hectares of semi-arid and arid rangelands. Its extensive taproot draws down deep water tables, while allelopathic chemicals suppress native perennial grasses."
    },
    {
        "id": 39,
        "topic": "Deforestation & Mining",
        "difficulty": "Hard",
        "question": "What is the phenomenon where repetitive annual forest fires destroy understory seed banks and convert moist deciduous forests into scrublands?",
        "options": ["Retrogressive plant succession", "Primary xerarch sere", "Climax homeostasis", "Ecosystem speciation"],
        "correct": 0,
        "explanation": "Recurring wildfires kill regenerating tree seedlings and destroy surface humus, driving 'retrogressive succession' where high-biomass forests degrade step-by-step into fire-hardy thorny scrub or barren rocky outcrops."
    },
    {
        "id": 40,
        "topic": "Deforestation & Mining",
        "difficulty": "Medium",
        "question": "In the Iron Ore mining belt of Goa and Bellary (Karnataka), what is the primary threat to surrounding water bodies and paddy lands?",
        "options": ["Siltation by fine iron ore rejects washed into rivers during monsoons", "Methane gas explosions", "Radioactive tailings runoff", "Excess nitrogen discharge"],
        "correct": 0,
        "explanation": "Heavy torrential rains wash uncovered, steeply sloped mine overburden and reject dumps into adjoining streams, rivers, and low-lying Khazan farmland, coating soils in sterile ferruginous slime."
    },

    # Topic 5: Sustainable Land Management, Policy & Bonn Challenge
    {
        "id": 41,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Easy",
        "question": "Under the Bonn Challenge, India pledged to restore how many million hectares of degraded and deforested land by 2030?",
        "options": ["5 million hectares", "10 million hectares", "26 million hectares", "50 million hectares"],
        "correct": 2,
        "explanation": "At UNCCD COP14 hosted in New Delhi in 2019, India's Prime Minister announced an enhanced national target to restore 26 million hectares of degraded and deforested land by the year 2030 (up from an earlier 21 million ha target)."
    },
    {
        "id": 42,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Medium",
        "question": "What is the core target concept of UN Sustainable Development Goal (SDG) Target 15.3 regarding land?",
        "options": ["Land Degradation Neutrality (LDN)", "Zero agricultural pesticide usage", "100% urban green roofs", "Doubling global timber exports"],
        "correct": 0,
        "explanation": "SDG Target 15.3 commits the world to achieve 'Land Degradation Neutrality' (LDN) by 2030, which means the amount and quality of land resources necessary to support ecosystem functions remains stable or increases."
    },
    {
        "id": 43,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Hard",
        "question": "What international declaration was adopted during UNCCD COP14 held in New Delhi in September 2019?",
        "options": ["The New Delhi Declaration: Investing in Land and Unlocking Opportunities", "The Paris Accord", "The Kyoto Protocol", "The Ramsar Convention"],
        "correct": 0,
        "explanation": "The New Delhi Declaration committed 196 participating countries to enhance transformative projects for land restoration, drought preparedness, community land rights, and empowering women in sustainable land stewardship."
    },
    {
        "id": 44,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Easy",
        "question": "What flagship scheme launched by the Government of India in 2015 provides farmers with field-specific nutrient test reports and fertilizer recommendations?",
        "options": ["Soil Health Card Scheme", "Pradhan Mantri Fasal Bima Yojana", "PM KISAN", "Kisan Credit Card"],
        "correct": 0,
        "explanation": "The Soil Health Card Scheme evaluates 12 critical parameters (N, P, K, S, Zn, Fe, Cu, Mn, Bo, pH, EC, OC) to advise farmers on balanced fertilizer dosage and prevent soil chemical degradation."
    },
    {
        "id": 45,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Medium",
        "question": "What does the Watershed Development Component of Pradhan Mantri Krishi Sinchayee Yojana (PMKSY-WDC) prioritize?",
        "options": ["Ridge-to-valley soil and moisture conservation treatment", "Deep tube well drilling", "Subsidizing chemical pesticides", "Constructing mega hydroelectric dams"],
        "correct": 0,
        "explanation": "PMKSY-WDC follows the scientific 'Ridge-to-Valley' principle: upper ridge catchments are treated first with contour trenches and afforestation to slow runoff before constructing gully plugs and farm ponds downstream in valley floors."
    },
    {
        "id": 46,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Hard",
        "question": "What traditional community-managed rainfed watershed village in Ahmednagar, Maharashtra is internationally celebrated as a model for drought reversal and water security?",
        "options": ["Ralegan Siddhi (and Hiware Bazar)", "Kaza", "Mawlynnong", "Punsari"],
        "correct": 0,
        "explanation": "Under the leadership of Anna Hazare in Ralegan Siddhi and Popatrao Pawar in Hiware Bazar, community watershed management (contour bunding, ban on open grazing, check dams, and banning water-intensive sugarcane) converted drought-stricken villages into self-sustaining water-surplus ecosystems."
    },
    {
        "id": 47,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Easy",
        "question": "Which high-efficiency micro-irrigation system delivers water directly to crop root zones, reducing evaporation and preventing waterlogging?",
        "options": ["Drip irrigation", "Flood irrigation", "Furrow irrigation", "Canal inundation"],
        "correct": 0,
        "explanation": "Drip irrigation achieves 90-95% water application efficiency by emitting water drops directly at plant roots, drastically cutting water use, preventing weed proliferation, and eliminating waterlogging risks."
    },
    {
        "id": 48,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Medium",
        "question": "What carbon-rich charcoal-like substance produced by pyrolyzing agricultural biomass is incorporated into degraded soils to boost moisture retention and microbial activity?",
        "options": ["Biochar", "Anthracite coal", "Fly ash", "Slag"],
        "correct": 0,
        "explanation": "Biochar has an enormous specific surface area and microporosity. When blended into sandy or degraded soils, it sequesters recalcitrant carbon for centuries while dramatically increasing cation exchange capacity (CEC) and moisture retention."
    },
    {
        "id": 49,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Hard",
        "question": "What are the three core biophysical indicators officially agreed upon by UNCCD to monitor Land Degradation Neutrality (LDN)?",
        "options": [
            "Land Cover, Land Productivity Dynamics (NPP), and Soil Organic Carbon (SOC)",
            "Rainfall volume, Air temperature, and Wind speed",
            "Forest area, Urban population, and GDP growth",
            "Nitrogen fertilizer, Pesticide residues, and Crop price"
        ],
        "correct": 0,
        "explanation": "Under UNCCD Decision 22/COP.11 and SDG Indicator 15.3.1, countries measure three sub-indicators: (1) Land Cover Change, (2) Land Productivity (via satellite-derived normalized difference vegetation index NDVI), and (3) Soil Organic Carbon (SOC) stocks."
    },
    {
        "id": 50,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Easy",
        "question": "What agricultural practice involves planting alternating strips of erosion-susceptible row crops (like maize) with erosion-resisting dense crops (like pulses/grasses)?",
        "options": ["Strip cropping", "Monocropping", "Clear cutting", "Deep tillage"],
        "correct": 0,
        "explanation": "Strip cropping alternates strips of dense, close-growing crops (like cowpea, groundnut, or clover) with open row crops. The dense strips filter sediment and break the speed of water runoff across the field."
    },
    {
        "id": 51,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Medium",
        "question": "What is the primary role of leguminous crops (such as chickpea, lentil, and mung bean) in restoring exhausted agricultural soils?",
        "options": [
            "Biological nitrogen fixation through symbiotic Rhizobium bacteria in root nodules",
            "Excreting toxic repellents to deter earthworms",
            "Absorbing all ground moisture to dry out wetlands",
            "Releasing heavy metals into the atmosphere"
        ],
        "correct": 0,
        "explanation": "Legumes host symbiotic Rhizobium bacteria in their root nodules, which fix inert atmospheric nitrogen (N2) into plant-available ammonium and nitrates, replenishing soil nitrogen naturally without synthetic urea."
    },
    {
        "id": 52,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Hard",
        "question": "In conservation agriculture, what are the three interdependent agronomic pillars?",
        "options": [
            "Minimum mechanical soil disturbance (zero tillage), Permanent organic soil cover, and Crop diversification",
            "Deep disc ploughing, Chemical burning of crop residue, and Continuous monoculture",
            "100% canal irrigation, High doses of synthetic urea, and Genetically modified hybrid seeds",
            "Deforestation, Heavy machinery compaction, and Flooding"
        ],
        "correct": 0,
        "explanation": "Conservation Agriculture (FAO standard) rests on three pillars: (1) Zero or minimum tillage to preserve soil aggregate architecture, (2) Retaining at least 30% crop residue cover on the surface to shield against erosion, and (3) Multi-species crop rotations and cover crops."
    },
    {
        "id": 53,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Easy",
        "question": "What is the natural process called when bare rock or degraded land is gradually colonized by pioneer lichens and mosses, slowly creating fertile soil?",
        "options": ["Ecological succession", "Eutrophication", "Salinization", "Soil liquefaction"],
        "correct": 0,
        "explanation": "Ecological succession is the progressive development of ecological communities over time. Primary succession on barren surfaces starts with pioneer crustose lichens that break down minerals into the earliest layers of organic soil."
    },
    {
        "id": 54,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Medium",
        "question": "What is the target year set by the United Nations for achieving a Land Degradation-Neutral world under SDG 15?",
        "options": ["2025", "2030", "2045", "2050"],
        "correct": 1,
        "explanation": "SDG Target 15.3 explicitly states: 'By 2030, combat desertification, restore degraded land and soil, including land affected by desertification, drought and floods, and strive to achieve a land degradation-neutral world.'"
    },
    {
        "id": 55,
        "topic": "Restoration, Policy & Bonn Challenge",
        "difficulty": "Hard",
        "question": "What satellite platform developed by ISRO's National Remote Sensing Centre (NRSC) provides public web access to geospatial environmental and natural resource datasets in India?",
        "options": ["Bhuvan (bhuvan.nrsc.gov.in)", "Google Earth Engine", "Copernicus Hub", "USGS EarthExplorer"],
        "correct": 0,
        "explanation": "Bhuvan is ISRO's premier Indian Geo-platform, delivering multi-sensor satellite imagery, thematic layers on land degradation, desertification atlases, water bodies, and wasteland monitoring tools for India."
    }
]

print(f"Total carefully authored quiz questions: {len(quiz_questions)}")

# Breakdown counts
topics = {}
diffs = {}
for q in quiz_questions:
    topics[q["topic"]] = topics.get(q["topic"], 0) + 1
    diffs[q["difficulty"]] = diffs.get(q["difficulty"], 0) + 1

print("Topics breakdown:", topics)
print("Difficulty breakdown:", diffs)

with open("quiz_questions.json", "w", encoding="utf-8") as f:
    json.dump(quiz_questions, f, indent=2)

print("Saved quiz_questions.json successfully!")
