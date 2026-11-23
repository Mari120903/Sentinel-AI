
from search import test_connection
from reader import read_page
from processor import clean_text, split_text
from memory import save_memory, load_memory

print("=" * 40)
print("Sentinel AI v0.1")
print("=" * 40)

test_connection()

print("\n[Reader] Leyendo página...")

content = read_page("https://example.com")

if content:
    print("\n[Processor] Limpiando contenido...")

    cleaned = clean_text(content)

    print("\n[Processor] Dividiendo contenido...")

    chunks = split_text(cleaned, chunk_size=50, overlap=10)

    print(f"\nCantidad de fragmentos: {len(chunks)}")

    memory = load_memory()

    if "reading_history" not in memory:
        memory["reading_history"] = []

    memory["reading_history"].append({
        "url": "https://example.com",
        "chunks": chunks
    })

    save_memory(memory)

    print("\n[Memory] Información guardada correctamente.")

else:
    print("No se pudo leer la página.")
