import json
import os
import datetime

# Load existing database
with open('database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# 1. Citizen Reports initial verified / under-review data
db['citizenReports'] = [
    {
        "id": "rep-101",
        "title": "Unregulated Sand Mining along Chambal River Bank",
        "category": "Soil Erosion & Riverbed Mining",
        "state": "Madhya Pradesh",
        "district": "Morena",
        "lat": 26.6984,
        "lng": 78.0125,
        "description": "Heavy earthmovers extracting alluvial sand near ravine fringes, accelerating bank erosion and threatening gharial nesting grounds.",
        "severity": "High",
        "date": "2026-11-12",
        "reporter": "Praveen Sharma (Local Panchayat Member)",
        "status": "Verified",
        "imageUrl": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=600&auto=format&fit=crop&q=80",
        "adminNotes": "Forwarded to State Pollution Control Board and Forest Department for site inspection."
    },
    {
        "id": "rep-102",
        "title": "Severe Canal Seepage and Waterlogging in Farmland",
        "category": "Waterlogging & Salinity",
        "state": "Punjab",
        "district": "Muktsar",
        "lat": 30.4746,
        "lng": 74.5167,
        "description": "Sub-surface canal leakage has raised saline water tables within 0.5 meters of surface, preventing wheat sowing across 45 hectares.",
        "severity": "Very High",
        "date": "2026-11-15",
        "reporter": "Gurmeet Singh (Kisan Union)",
        "status": "Under Review",
        "imageUrl": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=600&auto=format&fit=crop&q=80",
        "adminNotes": "Site coordinates logged. Drainage department engineer requested to inspect seepage."
    },
    {
        "id": "rep-103",
        "title": "Scrub Forest Clearing on Aravalli Hill Slope",
        "category": "Deforestation & Vegetative Depletion",
        "state": "Rajasthan",
        "district": "Alwar",
        "lat": 27.5530,
        "lng": 76.6346,
        "description": "Illegal clearing of native Dhok (Anogeissus pendula) trees for commercial real-estate encroachments along ridge line.",
        "severity": "High",
        "date": "2026-11-17",
        "reporter": "Ananya Sen (Aravalli Watch Volunteer)",
        "status": "Verified",
        "imageUrl": "https://images.unsplash.com/photo-1511497584788-87676104235f?w=600&auto=format&fit=crop&q=80",
        "adminNotes": "Verified against Sentinel-2 L2A optical baseline. Deputy Conservator of Forests notified."
    },
    {
        "id": "rep-104",
        "title": "Coastal Mangrove Die-off from Excessive Salinity Intrusion",
        "category": "Salinity / Ecosystem Stress",
        "state": "West Bengal",
        "district": "South 24 Parganas",
        "lat": 21.9497,
        "lng": 88.9004,
        "description": "Reduced freshwater river discharge causing salt encrustation on aerial pneumatophore roots along tidal creeks.",
        "severity": "Moderate",
        "date": "2026-11-18",
        "reporter": "Subhash Halder (Estuarine Biologist)",
        "status": "Submitted",
        "imageUrl": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=600&auto=format&fit=crop&q=80",
        "adminNotes": "Awaiting satellite spectral verification via NDWI time-series."
    }
]

# 2. Satellite Hotspot Observations & Temporal Benchmarks
db['satelliteHotspots'] = [
    {
        "id": "hotspot-thar",
        "name": "Thar Desert Margin (Dune Migration)",
        "state": "Rajasthan",
        "district": "Jaisalmer / Barmer",
        "lat": 26.9157,
        "lng": 70.9083,
        "zoom": 12,
        "primaryProcess": "Wind Deflation & Sand Dune Shifting",
        "observationCycles": {
            "2017": {"ndvi": 0.08, "cover": "Active Sand Dunes / Sparse Scrub", "cloudCover": "1.2%"},
            "2021": {"ndvi": 0.09, "cover": "Shelterbelt Stabilized Sand", "cloudCover": "0.8%"},
            "2024": {"ndvi": 0.12, "cover": "CAZRI Acacia & Cenchrus Grassland", "cloudCover": "2.1%"}
        },
        "description": "Multi-decadal satellite monitoring shows active sand dune movement stabilized by Indira Gandhi Canal command afforestation and shelterbelts."
    },
    {
        "id": "hotspot-chambal",
        "name": "Chambal Badlands & Ravine Expansion",
        "state": "Madhya Pradesh",
        "district": "Bhind / Morena",
        "lat": 26.7020,
        "lng": 78.4520,
        "zoom": 13,
        "primaryProcess": "Gully & Ravine Erosion",
        "observationCycles": {
            "2017": {"ndvi": 0.16, "cover": "Deep Gully Formations", "cloudCover": "3.5%"},
            "2021": {"ndvi": 0.19, "cover": "Check Dam Catchment Vegetation", "cloudCover": "1.1%"},
            "2024": {"ndvi": 0.23, "cover": "Bamboo Plantation Reclamation", "cloudCover": "2.4%"}
        },
        "description": "Alluvial soft soil subjected to intense monsoonal runoff, carving gorges up to 30 meters deep. Community contour bunding is slowing expansion."
    },
    {
        "id": "hotspot-sambhar",
        "name": "Sambhar Salt Lake Desiccation & Salinization",
        "state": "Rajasthan",
        "district": "Jaipur / Nagaur",
        "lat": 26.9124,
        "lng": 75.0065,
        "zoom": 12,
        "primaryProcess": "Soil Salinity & Water Surface Retraction",
        "observationCycles": {
            "2017": {"ndvi": 0.04, "ndwi": 0.35, "cover": "Inundated Salt Basin", "cloudCover": "0.4%"},
            "2021": {"ndvi": 0.03, "ndwi": 0.18, "cover": "Contracted Brine Pan", "cloudCover": "1.0%"},
            "2024": {"ndvi": 0.05, "ndwi": 0.22, "cover": "Partial Recharge Post-Monsoon", "cloudCover": "1.8%"}
        },
        "description": "Ramsar wetland experiencing drastic brine contraction and illegal salt pan encroachments as captured by Sentinel-2 SWIR and NDWI bands."
    },
    {
        "id": "hotspot-sundarbans",
        "name": "Sundarbans Coastal Erosion & Mangrove Stress",
        "state": "West Bengal",
        "district": "South 24 Parganas",
        "lat": 21.8200,
        "lng": 88.8500,
        "zoom": 11,
        "primaryProcess": "Saline Inundation & Wave Erosion",
        "observationCycles": {
            "2017": {"ndvi": 0.62, "cover": "Dense Tidal Forest", "cloudCover": "4.2%"},
            "2021": {"ndvi": 0.54, "cover": "Post-Cyclone Amphan Canopy Damage", "cloudCover": "6.8%"},
            "2024": {"ndvi": 0.59, "cover": "Regenerating Rhizophora Canopy", "cloudCover": "5.1%"}
        },
        "description": "Cyclonic storm surges and high salinity ingress degrading interior mangrove canopies, monitored via Sentinel-2 Red Edge bands."
    },
    {
        "id": "hotspot-muktsar",
        "name": "South-West Punjab Saline Waterlogging",
        "state": "Punjab",
        "district": "Fazilka / Muktsar",
        "lat": 30.2200,
        "lng": 74.2800,
        "zoom": 12,
        "primaryProcess": "Waterlogging & Sub-surface Soil Salinization",
        "observationCycles": {
            "2017": {"ndvi": 0.38, "cover": "Extensive Standing Water / Salt Crust", "cloudCover": "2.0%"},
            "2021": {"ndvi": 0.44, "cover": "Sub-surface Drainage Interventions", "cloudCover": "1.4%"},
            "2024": {"ndvi": 0.49, "cover": "Rehabilitated Mustard / Wheat Crops", "cloudCover": "2.8%"}
        },
        "description": "Flat terrain with impermeable subsoil clay layers trapping canal irrigation runoff. High water table evaporation precipitates sodium salts."
    }
]

# 3. Satellite Data Sources Configuration
db['satelliteProviders'] = [
    {
        "id": "esri-world-imagery",
        "name": "Esri World Imagery",
        "type": "High-Resolution Optical Basemap",
        "source": "Maxar, Earthstar Geographics, CNES/Airbus DS, USGS, AeroGRID, IGN, GIS User Community",
        "resolution": "0.3m to 15m (Seamless Global Multi-Resolution)",
        "refreshRate": "Annual to Multi-Annual Composites",
        "license": "Esri Master License Agreement / Educational & Public Visualization",
        "status": "Operational",
        "urlTemplate": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    },
    {
        "id": "nasa-gibs-modis",
        "name": "NASA GIBS Terra / MODIS Corrected Reflectance",
        "type": "Near-Real-Time (NRT) Daily Global True Color",
        "source": "NASA Earth Science Data and Information System (ESDIS)",
        "resolution": "250 meters",
        "refreshRate": "Daily (Observation latency: 3-5 hours post-orbit)",
        "license": "NASA Open Data Policy (Public Domain)",
        "status": "Operational",
        "urlTemplate": "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/MODIS_Terra_CorrectedReflectance_TrueColor/default/{date}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg"
    },
    {
        "id": "nasa-gibs-viirs",
        "name": "NASA GIBS Suomi NPP / VIIRS True Color",
        "type": "Near-Real-Time Day/Night Band & Surface Reflectance",
        "source": "NASA ESDIS / NOAA",
        "resolution": "375 meters",
        "refreshRate": "Daily Global Coverage",
        "license": "Open Data (Public Domain)",
        "status": "Operational",
        "urlTemplate": "https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/VIIRS_SNPP_CorrectedReflectance_TrueColor/default/{date}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg"
    },
    {
        "id": "copernicus-sentinel2",
        "name": "ESA Copernicus Sentinel-2 MSI",
        "type": "Multispectral 13-Band Optical Earth Observation",
        "source": "European Space Agency (ESA) & European Commission",
        "resolution": "10m (RGB, NIR), 20m (Red Edge, SWIR), 60m (Atmospheric)",
        "refreshRate": "5-day constellation revisit frequency over India",
        "license": "Copernicus Open Access Free & Open License",
        "status": "Operational",
        "urlTemplate": "Copernicus Data Space Ecosystem / Open WMS"
    },
    {
        "id": "isro-resourcesat",
        "name": "ISRO Resourcesat-2A LISS-IV & AWiFS",
        "type": "National Land Degradation & Natural Resource Sensors",
        "source": "National Remote Sensing Centre (NRSC) / ISRO Hyderabad",
        "resolution": "5.8m (LISS-IV), 23.5m (LISS-III), 56m (AWiFS)",
        "refreshRate": "5-day (AWiFS), 24-day (LISS-IV)",
        "license": "Government of India National Geospatial Policy 2022",
        "status": "Atlas Integrated Baseline",
        "urlTemplate": "ISRO Bhuvan Web Mapping Service (WMS)"
    }
]

# Write back database.json
with open('database.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2)

print(f"Successfully seeded database with {len(db['citizenReports'])} citizen reports, {len(db['satelliteHotspots'])} satellite hotspots, and {len(db['satelliteProviders'])} satellite providers!")
