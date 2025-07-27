def detect_headings(blocks):
    sorted_blocks = sorted(blocks, key=lambda b: -b["font_size"])
    title = sorted_blocks[0]["text"]

    max_font = sorted_blocks[0]["font_size"]
    h1_thresh = max_font * 0.9
    h2_thresh = max_font * 0.75
    h3_thresh = max_font * 0.6

    outline = []

    for block in blocks:
        size = block["font_size"]
        if size >= h1_thresh:
            level = "H1"
        elif size >= h2_thresh:
            level = "H2"
        elif size >= h3_thresh:
            level = "H3"
        else:
            continue
        outline.append({
            "level": level,
            "text": block["text"],
            "page": block["page"]
        })
    
    return title, outline
