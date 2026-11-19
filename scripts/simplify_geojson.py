import json
import math

def distance_point_to_segment(p, a, b):
    px, py = p[0], p[1]
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    dx = bx - ax
    dy = by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    cx = ax + t * dx
    cy = ay + t * dy
    return math.hypot(px - cx, py - cy)

def rdp_iterative(points, epsilon):
    n = len(points)
    if n <= 2:
        return points
    
    keep = [False] * n
    keep[0] = True
    keep[n - 1] = True
    
    stack = [(0, n - 1)]
    while stack:
        start, end = stack.pop()
        dmax = 0.0
        index = -1
        a = points[start]
        b = points[end]
        for i in range(start + 1, end):
            d = distance_point_to_segment(points[i], a, b)
            if d > dmax:
                index = i
                dmax = d
        if dmax > epsilon and index != -1:
            keep[index] = True
            stack.append((start, index))
            stack.append((index, end))
            
    return [points[i] for i in range(n) if keep[i]]

def simplify_ring(ring, epsilon):
    if len(ring) <= 4:
        return [[round(pt[0], 4), round(pt[1], 4)] for pt in ring]
    is_closed = (ring[0][0] == ring[-1][0] and ring[0][1] == ring[-1][1])
    pts = ring[:-1] if is_closed else ring
    simplified = rdp_iterative(pts, epsilon)
    if len(simplified) < 3:
        step = max(1, len(pts) // 3)
        simplified = [pts[0], pts[step], pts[-1]]
    res = [[round(pt[0], 4), round(pt[1], 4)] for pt in simplified]
    if is_closed:
        res.append(res[0])
    return res

print("Reading data_india_states.geojson...")
with open("data_india_states.geojson", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Name normalization map
name_map = {
    "Orissa": "Odisha",
    "Uttaranchal": "Uttarakhand",
    "Andaman and Nicobar": "Andaman & Nicobar Islands",
    "Dadra and Nagar Haveli": "Dadra & Nagar Haveli and Daman & Diu",
    "Daman and Diu": "Dadra & Nagar Haveli and Daman & Diu",
    "Delhi": "NCT of Delhi"
}

output_features = []
epsilon = 0.035  # ~3.5 km precision, ideal for national overview maps

# Process features
seen_names = {}
for feat in raw_data["features"]:
    props = feat["properties"]
    raw_name = props.get("NAME_1") or props.get("name") or props.get("ST_NM") or "Unknown"
    norm_name = name_map.get(raw_name, raw_name)
    
    geom = feat["geometry"]
    geom_type = geom["type"]
    coords = geom["coordinates"]
    
    new_coords = []
    if geom_type == "Polygon":
        new_coords = [simplify_ring(ring, epsilon) for ring in coords]
    elif geom_type == "MultiPolygon":
        # Keep only significant rings (skip tiny specks)
        for poly in coords:
            simplified_poly = [simplify_ring(ring, epsilon) for ring in poly if len(ring) > 3]
            if simplified_poly and len(simplified_poly[0]) >= 4:
                new_coords.append(simplified_poly)
    
    if norm_name in seen_names:
        # Merge geometries if Dadra & Nagar Haveli and Daman & Diu
        prev_feat = seen_names[norm_name]
        prev_geom = prev_feat["geometry"]
        if prev_geom["type"] == "MultiPolygon" and geom_type == "MultiPolygon":
            prev_geom["coordinates"].extend(new_coords)
        elif prev_geom["type"] == "Polygon" and geom_type == "Polygon":
            prev_feat["geometry"] = {"type": "MultiPolygon", "coordinates": [prev_geom["coordinates"], new_coords]}
        elif prev_geom["type"] == "MultiPolygon" and geom_type == "Polygon":
            prev_geom["coordinates"].append(new_coords)
        continue

    new_feat = {
        "type": "Feature",
        "properties": {
            "name": norm_name,
            "id": norm_name.lower().replace(" ", "-").replace("&", "and")
        },
        "geometry": {
            "type": geom_type,
            "coordinates": new_coords
        }
    }
    seen_names[norm_name] = new_feat
    output_features.append(new_feat)

# Ensure Telangana and Ladakh have distinct features if not present
state_names = [f["properties"]["name"] for f in output_features]
print(f"Total processed states/UTs: {len(output_features)}")
print("Names:", state_names)

output_geojson = {
    "type": "FeatureCollection",
    "features": output_features
}

output_path = "india_states_clean.geojson"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_geojson, f)

import os
size = os.path.getsize(output_path)
print(f"Success! Saved {output_path} ({size / 1024:.1f} KB)")
