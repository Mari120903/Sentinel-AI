
from search import test_connection
from reader import read_page
from processor import clean_text, split_text
from memory import save_reading

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

    save_reading("https://example.com", chunks)

    print("\n[Memory] Información guardada correctamente.")

else:
    print("No se pudo leer la página.")
