import urllib.request
import json

candidates = [
    ('udseIcrUxvA', 'What is Soil (and Why is it Important)?', 'CrashCourse Geography', '10:48'),
    ('yQ2i1z3GJxc', 'Asia’s Vanishing Lands: Desertification Documentary', 'DW Planet A', '22:15'),
    ('WC_JPSIoTPc', 'The Monk, The Engineer, The Artificial Glacier', 'Sonam Wangchuk / HIAL', '14:28'),
    ('uUCD19mEliU', 'Would You Stay if Your Home Became a Desert?', 'National Geographic', '8:14'),
    ('E2RzuoQ1t7k', 'Surviving Deserts (Full Episode) | Hostile Planet', 'National Geographic', '47:12'),
    ('kE05xr95rso', 'If Rangelands Could Speak', 'UNCCD Official', '6:30')
]

valid_videos = []
for vid, title, channel, duration in candidates:
    url = f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=8) as res:
            d = json.loads(res.read().decode())
            print(f'[CONFIRMED WORKING] {vid}: "{d.get("title")}" by {d.get("author_name")}')
            valid_videos.append({
                "id": f"vid-{len(valid_videos)+1}",
                "title": d.get("title"),
                "channel": d.get("author_name"),
                "youtube_id": vid,
                "watch_url": f"https://www.youtube.com/watch?v={vid}",
                "embed_url": f"https://www.youtube.com/embed/{vid}?rel=0",
                "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
                "duration": duration,
                "description": f"Verified educational documentary produced by {d.get('author_name')} examining soil science, desertification, and climate adaptation."
            })
    except Exception as e:
        print(f'[FAIL] {vid}: {e}')

print(f"\nTotal verified working videos: {len(valid_videos)}")
if len(valid_videos) > 0:
    with open('educational_videos.json', 'w', encoding='utf-8') as f:
        json.dump(valid_videos, f, indent=2)
    print("Updated educational_videos.json successfully!")
else:
    print("Network unavailable or no videos validated - keeping existing educational_videos.json.")
