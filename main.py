import os
import json
from parser import extract_blocks
from classifier import detect_headings

INPUT_DIR = "input"
OUTPUT_DIR = "output"

print(f"[INFO] Scanning input folder: {INPUT_DIR}")
files = os.listdir(INPUT_DIR)
print(f"[INFO] Found files: {files}")

for file in files:
    if not file.endswith(".pdf"):
        print(f"[SKIP] Not a PDF: {file}")
        continue

    print(f"\n[PROCESSING] File: {file}")
    filepath = os.path.join(INPUT_DIR, file)
    
    try:
        blocks = extract_blocks(filepath)
        print(f"[INFO] Extracted {len(blocks)} blocks from {file}")
    except Exception as e:
        print(f"[ERROR] Could not extract blocks from {file}: {e}")
        continue

    title, outline = detect_headings(blocks)
    print(f"[INFO] Title Detected: {title}")
    print(f"[INFO] Headings Found: {len(outline)}")

    result = {
        "title": title,
        "outline": outline
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, file.replace(".pdf", ".json"))
    
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"[SUCCESS] Output written to: {out_path}")
    except Exception as e:
        print(f"[ERROR] Writing output for {file}: {e}")
