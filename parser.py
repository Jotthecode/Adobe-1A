import fitz  

def extract_blocks(filepath):
    doc = fitz.open(filepath)
    blocks = []
    for page_num, page in enumerate(doc):
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            text = ""
            font_sizes = []
            is_bold = False
            for line in block["lines"]:
                for span in line["spans"]:
                    text += span["text"] + " "
                    font_sizes.append(span["size"])
                    if "bold" in span["font"].lower():
                        is_bold = True
            if text.strip():
                blocks.append({
                    "text": text.strip(),
                    "font_size": max(font_sizes),
                    "bold": is_bold,
                    "page": page_num
                })
    return blocks
