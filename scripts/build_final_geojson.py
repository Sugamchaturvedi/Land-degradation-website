import json

# Load base clean geojson
with open("india_states_clean.geojson", "r", encoding="utf-8") as f:
    base_data = json.load(f)

# Load telangana and ladakh
with open("telangana.geojson", "r", encoding="utf-8") as f:
    tg_raw = json.load(f)

with open("ladakh.geojson", "r", encoding="utf-8") as f:
    ld_raw = json.load(f)

# Load states_data to get canonical names and ids
with open("states_data.json", "r", encoding="utf-8") as f:
    states_meta = json.load(f)

meta_by_name = {s["name"].lower(): s for s in states_meta}

# Prepare Telangana MultiPolygon
tg_polys = []
for feat in tg_raw["features"]:
    g = feat["geometry"]
    if g["type"] == "Polygon":
        # Keep polygon coordinates
        tg_polys.append(g["coordinates"])
    elif g["type"] == "MultiPolygon":
        tg_polys.extend(g["coordinates"])

tg_feature = {
    "type": "Feature",
    "properties": {
        "name": "Telangana",
        "id": "telangana"
    },
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": tg_polys
    }
}

# Prepare Ladakh MultiPolygon
ld_polys = []
for feat in ld_raw["features"]:
    g = feat["geometry"]
    if g["type"] == "Polygon":
        ld_polys.append(g["coordinates"])
    elif g["type"] == "MultiPolygon":
        ld_polys.extend(g["coordinates"])

ld_feature = {
    "type": "Feature",
    "properties": {
        "name": "Ladakh",
        "id": "ladakh"
    },
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": ld_polys
    }
}

# Assemble all features
final_features = []
for feat in base_data["features"]:
    name = feat["properties"]["name"]
    # Check if this state is in metadata
    final_features.append(feat)

# Add Telangana and Ladakh
final_features.append(tg_feature)
final_features.append(ld_feature)

# Link each feature with full properties for rapid Leaflet rendering
for feat in final_features:
    p = feat["properties"]
    name = p["name"]
    # Match metadata
    matched = None
    for s in states_meta:
        if s["name"].lower() == name.lower() or s["id"] == p.get("id"):
            matched = s
            break
        # Alternate checks
        if "jammu" in name.lower() and "jammu" in s["name"].lower():
            matched = s
            break
        if "andaman" in name.lower() and "andaman" in s["name"].lower():
            matched = s
            break
        if "dadra" in name.lower() and "dadra" in s["name"].lower():
            matched = s
            break
        if "delhi" in name.lower() and "delhi" in s["name"].lower():
            matched = s
            break
            
    if matched:
        p["id"] = matched["id"]
        p["name"] = matched["name"]
        p["type"] = matched["type"]
        p["region"] = matched["region"]
        p["capital"] = matched["capital"]
        p["total_area_mha"] = matched["total_area_mha"]
        p["degraded_area_mha"] = matched["degraded_area_mha"]
        p["degraded_pct"] = matched["degraded_pct"]
        p["severity"] = matched["severity"]
        p["primary_causes"] = matched["primary_causes"]
        p["dominant_processes"] = matched["dominant_processes"]
        p["historical_pct"] = matched["historical_pct"]
        p["prevention_measures"] = matched["prevention_measures"]
        p["active_schemes"] = matched["active_schemes"]
        p["data_source"] = matched["data_source"]
        p["source_year"] = matched["source_year"]

# Check feature count
print(f"Final GeoJSON feature count: {len(final_features)}")

final_geojson = {
    "type": "FeatureCollection",
    "features": final_features
}

output_path = "india_states.geojson"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(final_geojson, f)

import os
size = os.path.getsize(output_path)
print(f"Successfully generated {output_path} ({size / 1024:.1f} KB)")
