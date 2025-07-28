# Adobe-1A: PDF Outline Extractor

This project extracts a structured document outline (title + headings) from input PDFs. It was built as part of the Adobe India Hackathon – Round 1A.

## Approach

The solution follows a modular pipeline:

1. **Block Extraction** (`parser.py`): Reads each PDF and extracts blocks of text using `PyMuPDF` or `pdfplumber`, preserving text layout and page numbers.
2. **Heading Detection** (`classifier.py`): Classifies blocks as potential titles, H1s, H2s, or H3s based on heuristics or ML features like:
   - Font size
   - Boldness
   - Position on page
   - Sentence length
   - Keyword patterns
3. **Output Generation**: Produces a JSON file per PDF with this format:

```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Problem Setup", "page": 2 }
  ]
}
