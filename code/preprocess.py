import regex as re

def normalize_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_sanskrit(text, max_len=400, overlap=50):
    sentences = text.split("।")
    chunks = []
    current = ""

    for s in sentences:
        if len(current) + len(s) < max_len:
            current += s + "।"
        else:
            chunks.append(current.strip())
            current = s + "।"

    if current:
        chunks.append(current.strip())

    return chunks

if __name__ == "__main__":
    from ingest import load_document

    text = load_document( r"..\data\Rag-docs.docx")
    text = normalize_text(text)
    chunks = chunk_sanskrit(text)

    print("Total chunks:", len(chunks))
    print("Sample chunk:\n", chunks[0])
