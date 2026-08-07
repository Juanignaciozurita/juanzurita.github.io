"""
Run this script from the root of your JuanZurita.github.io folder:
    python download_portraits.py

It downloads the 9 economist portraits into courses/smith-to-simulation/img/
and is safe to re-run.
"""
import os, urllib.request

IMG_DIR = os.path.join("courses", "smith-to-simulation", "img")
os.makedirs(IMG_DIR, exist_ok=True)

PORTRAITS = {
    "adam_smith.jpg":   "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Adam_Smith_The_Muir_portrait.jpg/300px-Adam_Smith_The_Muir_portrait.jpg",
    "malthus.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Thomas_Robert_Malthus.jpg/300px-Thomas_Robert_Malthus.jpg",
    "ricardo.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Portrait_of_David_Ricardo_by_Thomas_Phillips.jpg/300px-Portrait_of_David_Ricardo_by_Thomas_Phillips.jpg",
    "marx.jpg":        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Karl_Marx_001.jpg/300px-Karl_Marx_001.jpg",
    "jevons.jpg":      "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/William_Stanley_Jevons.jpg/300px-William_Stanley_Jevons.jpg",
    "keynes.jpg":      "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/John_Maynard_Keynes.jpg/300px-John_Maynard_Keynes.jpg",
    "solow.jpg":       "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Robert_Solow_by_Olaf_Storbeck.jpg/300px-Robert_Solow_by_Olaf_Storbeck.jpg",
    "lucas.jpg":       "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Robert_Lucas.jpg/300px-Robert_Lucas.jpg",
    "piketty.jpg":     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Thomas_Piketty%2C_2015_%28cropped%29.jpg/300px-Thomas_Piketty%2C_2015_%28cropped%29.jpg",
}

for filename, url in PORTRAITS.items():
    dest = os.path.join(IMG_DIR, filename)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"  skip  {filename} (already exists)")
        continue
    print(f"  downloading {filename} ...", end=" ")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=15).read()
        with open(dest, "wb") as f:
            f.write(data)
        print(f"OK ({len(data):,} bytes)")
    except Exception as e:
        print(f"FAILED: {e}")

print("\nDone. Now update index.qmd to use img/<name>.jpg paths.")
