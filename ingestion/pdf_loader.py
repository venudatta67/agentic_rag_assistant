from pypdf import PdfReader

def load_pdf(path: str):
    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            pages.append({
                "page_number": i + 1,
                "text": text
            })
    return pages
