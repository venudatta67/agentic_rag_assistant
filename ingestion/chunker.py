import re

def semantic_chunk(pages):
    chunks = []
    chunk_id = 0

    for page in pages:
        sections = re.split(r"\n(?=[A-Z][A-Za-z ]{5,})", page["text"])
        for section in sections:
            if len(section.strip()) < 200:
                continue

            chunk_id += 1
            chunks.append({
                "chunk_id": f"chunk_{chunk_id}",
                "text": section.strip(),
                "section": section.split("\n")[0][:100],
                "page": page["page_number"]
            })

    return chunks
