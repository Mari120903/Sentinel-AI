import re


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def split_text(text, chunk_size=200, overlap=20):
    if chunk_size <= 0:
        raise ValueError("chunk_size debe ser mayor que cero")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap debe ser mayor o igual a cero y menor que chunk_size")

    words = text.split()
    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

if __name__ == "__main__":
    sample = "Sentinel AI procesa información. " * 30

    cleaned = clean_text(sample)
    chunks = split_text(cleaned, chunk_size=20, overlap=5)

    print(f"Cantidad de fragmentos: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"\nFragmento {i + 1}:")
        print(chunk)