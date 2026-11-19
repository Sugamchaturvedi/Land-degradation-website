import json

solutions_data = [
    {
        "id": "afforestation-reforestation",
        "title": "Afforestation & Assisted Natural Regeneration (ANR)",
        "category": "Biological & Vegetative",
        "icon": "fa-tree",
        "tagline": "Rebuilding forest canopy and underground biological root anchors",
        "what_it_means": "Afforestation is the establishment of a forest or stand of trees in an area where there was previously no forest cover, whereas reforestation replants degraded or depleted forest tracts.",
        "how_it_works": "The multi-tiered tree canopy intercepts falling raindrops, reducing kinetic energy by up to 85%. Tree roots physically bind soil aggregates together and form mycorrhizal fungal networks that increase macro-porosity and humus formation, promoting rapid water infiltration into deep groundwater aquifers.",
        "where_it_is_useful": "Steep mountain slopes in the Himalayas and Western Ghats; degraded mining overburden in Central India; riparian buffer strips along rivers; wind-swept marginal boundaries of the Thar Desert.",
        "environmental_benefits": "Sequesters 2 to 4 tons of atmospheric CO2 per hectare annually; builds topsoil organic carbon; halts surface runoff; restores micro-climate and humidity; preserves critically endangered avian and insect biodiversity.",
        "practical_implementation": [
            "Conduct baseline soil testing (pH, texture, bulk density) and select indigenous climate-hardy species (e.g., Azadirachta indica, Acacia nilotica, Dalbergia sissoo, Madhuca longifolia). Avoid monoculture alien plantations like Eucalyptus on drylands.",
            "Establish contour trenches or V-shaped micro-catchments before planting to maximize monsoon water retention.",
            "Plant 1-to-2-year-old hardened nursery saplings at spacing of 3m x 3m during early onset of the monsoon.",
            "Install protective tree guards or community-monitored live fences (e.g., Agave americana, Euphorbia) to exclude livestock grazing during the first 3 critical years.",
            "Apply biochar and organic vermicompost to planting pits to stimulate mycorrhizal root colonization."
        ],
        "case_study": "Telanganaku Haritha Haram initiative planted over 2.4 billion seedlings across Telangana, elevating green cover from 24% to 33.2% between 2015 and 2022."
    },
    {
        "id": "contour-farming-terracing",
        "title": "Contour Farming & Bench Terracing",
        "category": "Mechanical & Structural",
        "icon": "fa-layer-group",
        "tagline": "Re-engineering hill slopes into staircases of moisture conservation",
        "what_it_means": "Contour farming involves ploughing, seeding, and cultivating across the slope along contour lines of equal elevation rather than up and down. Bench terracing converts steep hillsides into a series of stepped level platforms.",
        "how_it_works": "By breaking the continuous downward gradient into short, flat stretches, water runoff velocity is reduced from torrential destructive speeds down to non-erosive levels. Water is trapped on each step and given time to infiltrate rather than shearing away topsoil.",
        "where_it_is_useful": "Sloping terrains of Himachal Pradesh, Uttarakhand, Nilgiris, Nagaland, and Meghalaya with slope gradients between 5% and 35%.",
        "environmental_benefits": "Cuts topsoil erosion by 75% to 90%; retains 40% to 60% more seasonal rainfall within the root zone; mitigates downstream flash floods and riverbed sedimentation.",
        "practical_implementation": [
            "Survey slope contours using an A-frame or Hydro-level to establish accurate horizontal baseline markings.",
            "Excavate inward-sloping bench terraces with a 1:1 riser slope reinforced with dry stone masonry or dense vetiver hedgerows.",
            "Maintain a shoulder bund (30 cm height) on the outer edge of each terrace to retain standing rainwater.",
            "Construct a gently graded drainage chute at the inner edge to safely lead overflow surplus to a water-harvesting farm pond.",
            "Maintain permanent green grass cover (e.g., Cenchrus ciliaris, Guinea grass) on the vertical terrace risers."
        ],
        "case_study": "ICAR-IISWC watershed projects in Dehradun foothills demonstrated a reduction in runoff from 42% to 11% of annual precipitation via bench terracing."
    },
    {
        "id": "micro-irrigation",
        "title": "Precision Micro-Irrigation (Drip & Sprinkler)",
        "category": "Agronomic & Technological",
        "icon": "fa-tint",
        "tagline": "Delivering drop-by-drop hydration straight to plant root zones",
        "what_it_means": "Micro-irrigation comprises targeted low-pressure irrigation systems that distribute water directly to the plant root zone via a network of drippers, emitters, or micro-sprinklers instead of flooding the entire field surface.",
        "how_it_works": "Unlike conventional flood irrigation where 50-60% of water is lost to deep percolation and evaporation, drip systems apply water at application rates matching plant transpiration needs, keeping soil moisture tension optimal and preventing water table rise.",
        "where_it_is_useful": "Water-scarce arid and semi-arid tracts of Rajasthan, Gujarat, Maharashtra, Karnataka, and Rayalaseema; horticultural orchards, cotton, sugarcane, and vegetables.",
        "environmental_benefits": "Saves 40% to 70% water compared to surface flooding; eliminates canal seepage and secondary soil salinization; cuts energy pumping costs by 30-40%; reduces nitrogen leaching into groundwater.",
        "practical_implementation": [
            "Test irrigation water electrical conductivity (EC < 2.0 dS/m) and filter out silt through hydro-cyclone and disc filter assemblies.",
            "Lay UV-stabilized LLDPE lateral lines with pressure-compensating (PC) inline drippers spaced according to crop row geometry.",
            "Combine with fertigation tanks to meter liquid fertilizers directly into the drip stream in small, frequent dosages.",
            "Automate delivery cycles with soil moisture sensors (tensiometers) to trigger pulses only when soil matrix suction exceeds 30 kPa."
        ],
        "case_study": "Gujarat Green Revolution Company (GGRC) transitioned over 1.2 million hectares of farmland to micro-irrigation, reclaiming waterlogged canal commands in Saurashtra."
    },
    {
        "id": "crop-rotation-diversification",
        "title": "Crop Rotation & Leguminous Intercropping",
        "category": "Agronomic & Biological",
        "icon": "fa-seedling",
        "tagline": "Breaking mono-cropping depletion with biological nitrogen regeneration",
        "what_it_means": "The systematic planting of different crop types in sequential agricultural seasons on the same land, specifically alternating nutrient-exhaustive crops (cereals/cash crops) with soil-enriching leguminous and cover crops.",
        "how_it_works": "Deep-rooted and shallow-rooted crops alternate to draw nutrients from different depths of the soil profile. Legumes form root nodules hosting Rhizobium bacteria that biologically convert atmospheric nitrogen into plant-available nitrates, replenishing soil chemical fertility without synthetic chemicals.",
        "where_it_is_useful": "Indo-Gangetic Plain monoculture regions (Punjab, Haryana, Western UP suffering from continuous paddy-wheat rotation); Deccan plateau cotton-soybean belts.",
        "environmental_benefits": "Reduces synthetic nitrogen fertilizer demand by 30-50 kg/ha; suppresses soil-borne fungal pathogens, nematodes, and herbicide-resistant weeds; enhances soil microbial biomass and mycorrhizal networks.",
        "practical_implementation": [
            "Introduce a short-duration summer catch crop (e.g., Mung bean / Cowpea) between wheat harvesting and paddy transplanting in the Indo-Gangetic belt.",
            "Incorporate green manure crops like Sesbania aculeata (Dhaincha) or Crotalaria juncea (Sunnhemp) into the soil at the 45-day flowering stage.",
            "Adopt strip intercropping (e.g., 4 rows of Sorghum/Maize alternated with 2 rows of Pigeonpea/Groundnut).",
            "Inoculate legume seeds with Rhizobium and Phosphate Solubilizing Bacteria (PSB) biofertilizer before sowing."
        ],
        "case_study": "ICAR-CSSRI trials in Haryana showed that introducing Sesbania green manuring in a rice-wheat cycle increased soil organic carbon by 0.18% in three cropping seasons."
    },
    {
        "id": "controlled-grazing-silvopasture",
        "title": "Rotational Grazing & Silvopastoral Management",
        "category": "Biological & Management",
        "icon": "fa-horse",
        "tagline": "Protecting rangeland root mats while maximizing sustainable livestock forage",
        "what_it_means": "Silvopasture deliberately combines trees, forage pasture, and livestock on the same land unit, regulated through timed rotational grazing schedules to prevent pasture over-exploitation.",
        "how_it_works": "Subdividing pastures into smaller paddocks allows livestock to graze one section intensively for a short period before moving them to the next paddock. This gives grazed grasses ample time (30-60 days) to replenish root carbohydrates and regrow dense protective foliage before being grazed again.",
        "where_it_is_useful": "Arid and semi-arid grazing commons (Gochar / Oran lands) of Rajasthan, Gujarat, Madhya Pradesh, and alpine meadows (Bugyals) of Himachal and Uttarakhand.",
        "environmental_benefits": "Prevents soil compaction and pulverization caused by hooves; protects perennial desert grass species (Lasiurus scindicus - Sewan grass); prevents wind deflation and sheet wash.",
        "practical_implementation": [
            "Form village-level pasture management committees (Panchayat Oran committees) to enforce community grazing rules and rotational grazing calendars.",
            "Reseed degraded rangelands with indigenous drought-hardy grasses such as Cenchrus ciliaris (Dhaman) and Lasiurus scindicus (Sewan).",
            "Plant multipurpose fodder trees (e.g., Prosopis cineraria, Hardwickia binata, Leucaena leucocephala) at 10m x 10m spacing.",
            "Construct solar-powered borewell drinking troughs in paddock centers to prevent animals from crowding and trampling natural streams."
        ],
        "case_study": "CAZRI's silvopastoral model in Jodhpur generated 3.5 to 4.2 tons of dry nutritious fodder per hectare annually while stabilizing shifting sand dunes."
    },
    {
        "id": "rainwater-harvesting-checkdams",
        "title": "Decentralized Rainwater Harvesting & Check Dams",
        "category": "Hydrological & Structural",
        "icon": "fa-cloud-rain",
        "tagline": "Catching every falling raindrop to recharge exhausted aquifers",
        "what_it_means": "The collection and storage of surface runoff from rainfall events using localized decentralized structures such as check dams, percolation ponds, farm ponds (Khet Talab), and Johads.",
        "how_it_works": "Structures intercept ephemeral monsoon flash streams. By storing water for several months, hydrostatic pressure forces clean water down through porous fractures in the bedrock, replenishing depleted regional water tables and transforming seasonal dry wells into perennial water sources.",
        "where_it_is_useful": "Hard-rock granitic and basaltic terrain across Central India, Bundelkhand, Vidarbha, Rayalaseema, and Rajasthan.",
        "environmental_benefits": "Raises groundwater table by 1 to 5 meters across catchment zones; decreases mineral fluoride and salt concentration in well water; provides critical life-saving irrigation for winter (Rabi) crops.",
        "practical_implementation": [
            "Select check dam sites in 2nd or 3rd order natural streams with firm rock banks and a moderate gradient (less than 2%).",
            "Construct masonry or concrete overflow weirs with deep key trenches into bedrock to prevent undermining.",
            "Equip with boulder rip-rap apron on the downstream side to prevent scouring and energy undercutting.",
            "Encourage construction of individual farm ponds (e.g., 20m x 20m x 3m) lined with LDPE geo-membranes for localized supplementary irrigation."
        ],
        "case_study": "Tarun Bharat Sangh (led by Rajendra Singh) revived five dried perennial rivers (Arvari, Ruparel, Sarsa, Bhagani, Jahajwali) in Alwar, Rajasthan by building over 8,600 traditional earthen Johads."
    },
    {
        "id": "chemical-salinity-reclamation",
        "title": "Chemical Reclamation of Sodic Lands (Gypsum & Press-Mud)",
        "category": "Chemical & Remedial",
        "icon": "fa-flask",
        "tagline": "Neutralizing toxic alkaline crusts to restore arable soil structure",
        "what_it_means": "The application of chemical amendments, primarily agricultural-grade gypsum (CaSO4·2H2O), supplemented with organic amendments like sugar factory press-mud, to remediate high-pH sodic (Usar) soils.",
        "how_it_works": "Sodic soils have excessive exchangeable sodium (ESP > 15%) causing clay particles to disperse and seal off pores. Soluble Calcium from gypsum replaces sodium ions on the clay complex. The displaced sodium forms soluble sodium sulfate, which is flushed down beyond the root zone with ponded water, restoring soil aggregation and hydraulic conductivity.",
        "where_it_is_useful": "Indo-Gangetic alluvial plains of Uttar Pradesh, Haryana, Punjab, and coastal sodic lands of Gujarat, covering over 3.7 million hectares.",
        "environmental_benefits": "Lowers soil pH from toxic levels (pH > 10.0) down to productive levels (pH 7.8-8.4); increases water infiltration rate by 500%; restores productive multi-crop cultivation on previously abandoned wastelands.",
        "practical_implementation": [
            "Dig soil profile pits and determine Gypsum Requirement (GR) through laboratory titration of exchangeable sodium.",
            "Construct strong earthen perimeter bunds (30-40 cm high) around fields and laser-level the surface perfectly to ensure uniform ponding.",
            "Broadcast finely crushed agricultural gypsum (passing 2 mm sieve) at 50% of the laboratory-determined GR value and lightly harrow into top 10 cm.",
            "Pond fresh irrigation water to a depth of 10-15 cm continuously for 10 to 15 days to leach displaced sodium downward.",
            "Immediately transplant salt-tolerant rice varieties (CSR 30 or CSR 36) followed by wheat (KRL 210) with Sesbania green manuring."
        ],
        "case_study": "The UP Sodic Land Reclamation Project (UPSLRP III - World Bank funded) successfully reclaimed over 230,000 hectares of barren Usar land across 29 districts of Uttar Pradesh."
    },
    {
        "id": "watershed-management",
        "title": "Integrated Watershed Management (Ridge-to-Valley)",
        "category": "Comprehensive Integrated System",
        "icon": "fa-mountain",
        "tagline": "Harmonizing soil, water, forest, and human stewardship across natural drainage basins",
        "what_it_means": "A holistic approach that treats an entire hydrological drainage basin as a unified ecological system, deploying simultaneous mechanical, vegetative, and social interventions from the ridge line to the valley outlet.",
        "how_it_works": "Upper ridge slopes (steepest, highest erosion) are treated with continuous contour trenches (CCT) and dense afforestation to slow runoff velocity. Intermediate hillslopes are terraced with horticulture and agroforestry. Valley floors receive check dams, percolation tanks, and precision agriculture.",
        "where_it_is_useful": "All degraded semi-arid rainfed agro-ecosystems across India, particularly peninsular India and the Himalayan foothills.",
        "environmental_benefits": "Reduces catchment sediment yield by up to 80%; enhances total biomass productivity; insulates agrarian communities against multi-year drought cycles.",
        "practical_implementation": [
            "Delineate watershed boundaries using GIS, satellite DEM elevation maps, and drainage stream orders.",
            "Form Village Watershed Committees (VWC) ensuring democratic representation of landless families and women.",
            "Treat upper ridge areas first: continuous contour trenches, stone bunds, and aerial seeding of indigenous grasses and shrubs.",
            "Treat middle reaches: loose boulder gully plugs, farm bunding, and fruit tree orchards (guava, pomegranate, custard apple).",
            "Treat lower valley reaches: concrete check dams, silt retention basins, and community farm ponds."
        ],
        "case_study": "Hiware Bazar village in Maharashtra's drought-prone Ahmednagar district increased green cover from 15% to 85%, boosted average family income 20-fold, and eliminated distress seasonal migration."
    },
    {
        "id": "sand-dune-stabilization",
        "title": "Sand Dune Stabilization & Shelterbelts",
        "category": "Mechanical & Biological",
        "icon": "fa-wind",
        "tagline": "Taming wind-driven sand seas and stopping the eastward march of the Thar Desert",
        "what_it_means": "A two-phase technique that first establishes physical micro-windbreaks across shifting sand dunes and subsequently plants drought-hardy deep-rooted perennial trees and shrubs to permanently anchor the dune.",
        "how_it_works": "Erecting brushwood barriers in checkerboard patterns reduces wind velocity at the ground level below the threshold velocity required to dislodge sand grains (approx 16 km/h). Deep roots of planted perennial vegetation bind shifting sand into a stable profile.",
        "where_it_is_useful": "Active and semi-stabilized sand dunes of Western Rajasthan (Thar Desert), Kachchh (Gujarat), and southwest Haryana.",
        "environmental_benefits": "Protects transport highways, railway tracks, and the Indira Gandhi Canal from getting buried under shifting sand drifts; restores desert biodiversity.",
        "practical_implementation": [
            "Collect locally available brushwood (Crotalaria burhia, Leptadenia pyrotechnica, Calligonum polygonoides).",
            "Erect physical windbreak barriers buried 30 cm into the sand in 5m x 5m checkerboard squares perpendicular to prevailing southwesterly winds.",
            "Sow seeds of desert grasses (Lasiurus scindicus, Cenchrus ciliaris) along barriers with the first monsoon shower.",
            "Transplant containerized saplings of Acacia tortilis, Prosopis cineraria, and Tecomella undulata (Rohida) inside the stabilized checkerboard grids.",
            "Maintain strict fencing against grazing camels, goats, and cattle for a minimum of 5 years."
        ],
        "case_study": "CAZRI stabilized over 50,000 hectares of shifting sand dunes along the Indira Gandhi Nahar Project (IGNP) canal banks, preventing canal siltation."
    },
    {
        "id": "biochar-organic-amelioration",
        "title": "Biochar & Organic Soil Amelioration",
        "category": "Soil Biology & Carbon Sequestration",
        "icon": "fa-recycle",
        "tagline": "Converting farm residue into centuries-stable recalcitrant carbon sponges",
        "what_it_means": "The pyrolysis (high-temperature thermal breakdown in low oxygen) of crop residues (paddy straw, cotton stalks, bagasse) into a stable, porous carbon material (biochar) blended into degraded soil with compost and bio-fertilizers.",
        "how_it_works": "Biochar has high specific surface area (>300 m2/g) and microporosity. It acts as a permanent sponge that retains water and dissolved nutrients, prevents nutrient leaching, and creates micro-habitats protecting beneficial soil bacteria and mycorrhizal fungi.",
        "where_it_is_useful": "Paddy straw burning regions of Punjab and Haryana; eroded red and lateritic soils of Eastern and Southern India; coarse sandy soils.",
        "environmental_benefits": "Solves air pollution caused by crop stubble burning; sequesters 2.5 tons of carbon dioxide equivalent per ton of biochar applied; boosts soil moisture retention by 20-30%.",
        "practical_implementation": [
            "Collect surplus agricultural residues (paddy stubble, mustard stalks, cotton stalks) and dry below 15% moisture content.",
            "Process in closed flame-cap biochar kilns or continuous pyrolyzers at 450°C to 550°C.",
            "Quench biochar with water and crush to particle sizes between 1 mm and 4 mm.",
            "Inoculate biochar by co-composting with cattle manure, vermicompost, and liquid bio-fertilizers for 2-3 weeks before soil application.",
            "Apply at 5 to 10 tons per hectare and incorporate into the top 15 cm of soil during pre-monsoon field preparation."
        ],
        "case_study": "ICAR-IARI New Delhi field trials proved that combining biochar with vermicompost improved crop yield by 18-24% on coarse sandy soils while reducing irrigation requirements by 25%."
    }
]

news_data = [
    {
        "id": "news-1",
        "title": "MoEFCC Reaffirms India's Bonn Challenge Pledge: 26 Million Hectares Target by 2030",
        "date": "2024-03-12",
        "category": "Policy & National Missions",
        "source": "Ministry of Environment, Forest and Climate Change / PIB New Delhi",
        "summary": "India has reaffirmed its commitment under the Bonn Challenge and UNCCD COP14 New Delhi Declaration to bring 26 million hectares of degraded and deforested land into active restoration by 2030, leveraging integrated schemes like PMKSY, Green India Mission, and Nagar Van Yojana.",
        "url": "https://pib.gov.in/PressReleasePage.aspx?PRID=1858349",
        "tags": ["Bonn Challenge", "UNCCD", "MoEFCC", "Restoration"]
    },
    {
        "id": "news-2",
        "title": "ISRO Space Applications Centre Releases Updated Geospatial Desertification & Land Degradation Atlas",
        "date": "2023-11-20",
        "category": "Geospatial Intelligence",
        "source": "Space Applications Centre (SAC), ISRO Ahmedabad",
        "summary": "ISRO SAC published comprehensive multi-temporal satellite analyses indicating 97.85 million hectares (29.77% of India's TGA) undergo various land degradation processes, with water erosion and vegetation loss continuing to be dominant drivers across peninsular and central states.",
        "url": "https://www.sac.gov.in/Vyom/SACDesertification.jsp",
        "tags": ["ISRO", "Remote Sensing", "Land Degradation Atlas", "Bhuvan"]
    },
    {
        "id": "news-3",
        "title": "G20 Global Land Initiative Advances Collaborative Restoration Frameworks across South Asia",
        "date": "2024-01-18",
        "category": "International Cooperation",
        "source": "UNCCD / G20 Land Initiative Secretariat",
        "summary": "Building upon India's G20 Presidency priorities, the G20 Global Land Initiative launched capacity-building workshops on mining land rehabilitation, community forestry, and satellite-based land productivity monitoring for state forest departments.",
        "url": "https://www.unccd.int/g20-global-land-initiative",
        "tags": ["G20", "Global Land Initiative", "Capacity Building"]
    },
    {
        "id": "news-4",
        "title": "World Bank & Government of India Expand REWARD Project across Semi-Arid Watersheds",
        "date": "2023-09-05",
        "category": "Projects & Investments",
        "source": "World Bank / Department of Land Resources (DoLR)",
        "summary": "The Rejuvenating Watersheds for Agricultural Resilience through Innovative Development (REWARD) project expanded across Karnataka and Odisha, deploying high-resolution digital soil health maps and climate-resilient water harvesting protocols.",
        "url": "https://www.worldbank.org/en/news/press-release/2022/02/18/world-bank-funds-reward-watershed-project",
        "tags": ["World Bank", "REWARD", "Watershed", "Odisha", "Karnataka"]
    },
    {
        "id": "news-5",
        "title": "ICAR-CSSRI Deploys Solar Sub-Surface Drainage Across Waterlogged Canal Commands in Haryana & Punjab",
        "date": "2024-02-14",
        "category": "Scientific Innovation",
        "source": "ICAR Central Soil Salinity Research Institute, Karnal",
        "summary": "ICAR-CSSRI inaugurated new solar-powered sub-surface drainage (SSD) installations across 15,000 hectares of waterlogged saline agricultural farmland in Rohtak and Muktsar, achieving full root-zone salt evacuation within two cropping seasons.",
        "url": "https://cssri.res.in/",
        "tags": ["CSSRI", "Salinity Reclamation", "Sub-Surface Drainage"]
    },
    {
        "id": "news-6",
        "title": "Green Wall of India Initiative Commences Initial Phase Across Aravalli Ecological Corridor",
        "date": "2023-12-10",
        "category": "Afforestation & Biodiversity",
        "source": "Forest Departments of Haryana, Rajasthan, Gujarat",
        "summary": "Initial greening operations commenced along critical gaps in the Aravalli mountain belt covering southern Haryana and northeastern Rajasthan to halt the eastward drift of sand particles and recharge the National Capital Region's underground water aquifers.",
        "url": "https://moef.gov.in/",
        "tags": ["Green Wall of India", "Aravalli", "Sand Dune Barrier"]
    }
]

educational_videos = [
    {
        "id": "vid-1",
        "title": "Land Degradation Neutrality: Why Soil Health Matters for India and the World",
        "channel": "United Nations Convention to Combat Desertification (UNCCD)",
        "youtube_id": "r7c1F_B9Hqg",
        "embed_url": "https://www.youtube-nocookie.com/embed/r7c1F_B9Hqg",
        "duration": "4:32",
        "description": "An official UNCCD documentary explaining the principles of Land Degradation Neutrality (LDN) and how protecting healthy topsoil prevents forced climate migration and secures food security."
    },
    {
        "id": "vid-2",
        "title": "Combating Desertification: The Science of Land Restoration",
        "channel": "Food and Agriculture Organization (FAO)",
        "youtube_id": "rXm1-e6Qn9k",
        "embed_url": "https://www.youtube-nocookie.com/embed/rXm1-e6Qn9k",
        "duration": "5:18",
        "description": "FAO's masterclass on sustainable soil management, showcasing global case studies in afforestation, regenerative agriculture, and community-based land stewardship."
    },
    {
        "id": "vid-3",
        "title": "How Check Dams and Watershed Management Replaced Drought with Abundance",
        "channel": "Down To Earth / CSE India",
        "youtube_id": "4jVf_nC8Zps",
        "embed_url": "https://www.youtube-nocookie.com/embed/4jVf_nC8Zps",
        "duration": "9:45",
        "description": "Investigative report on how traditional rainwater harvesting and ridge-to-valley watershed treatment transformed dryland villages in Central and Western India into water-secure hubs."
    },
    {
        "id": "vid-4",
        "title": "Understanding Soil Salinization and Sodic Land Reclamation",
        "channel": "ICAR-CSSRI Educational Outreach",
        "youtube_id": "mQjF3kU2sW4",
        "embed_url": "https://www.youtube-nocookie.com/embed/mQjF3kU2sW4",
        "duration": "7:12",
        "description": "Scientific overview explaining how capillary water rise causes surface salt efflorescence and how agricultural gypsum and sub-surface drainage reclaim toxic Usar soils."
    },
    {
        "id": "vid-5",
        "title": "The Ice Stupas of Ladakh: Artificial Glaciers Greening the Cold Desert",
        "channel": "Rolex Awards / Himalayan Institute of Alternatives (HIAL)",
        "youtube_id": "w8jN2a3X1Yk",
        "embed_url": "https://www.youtube-nocookie.com/embed/w8jN2a3X1Yk",
        "duration": "6:20",
        "description": "Discover how engineer Sonam Wangchuk and Ladakhi youth build vertical ice stupas that freeze winter stream waste to water thousands of saplings and orchards in spring."
    },
    {
        "id": "vid-6",
        "title": "Satellite Remote Sensing for Desertification & Land Degradation Monitoring",
        "channel": "Indian Space Research Organisation (ISRO)",
        "youtube_id": "9tG7eX5Y8dQ",
        "embed_url": "https://www.youtube-nocookie.com/embed/9tG7eX5Y8dQ",
        "duration": "8:05",
        "description": "A technical lecture on how IRS AWiFS, LISS-III, and Bhuvan satellite datasets are analyzed using Normalized Difference Vegetation Index (NDVI) and thermal bands to generate national degradation atlases."
    }
]

with open("solutions_data.json", "w", encoding="utf-8") as f:
    json.dump(solutions_data, f, indent=2)

with open("news_data.json", "w", encoding="utf-8") as f:
    json.dump(news_data, f, indent=2)

with open("educational_videos.json", "w", encoding="utf-8") as f:
    json.dump(educational_videos, f, indent=2)

print("Saved solutions_data.json, news_data.json, and educational_videos.json successfully!")
