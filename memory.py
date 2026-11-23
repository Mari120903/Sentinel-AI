
import json
import os
from processor import normalize_text

# ==========================================
# 1. ALMACENAMIENTO
# ==========================================

def save_memory(data, filename="memory.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_memory(filename="memory.json"):
    if not os.path.exists(filename):
        return {}

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_reading(url, chunks, filename="memory.json"):
    memory = load_memory(filename)

    if "reading_history" not in memory:
        memory["reading_history"] = []

    for reading in memory["reading_history"]:
        if reading["url"] == url:
            reading["chunks"] = chunks
            save_memory(memory, filename)
            print("[Memory] Lectura actualizada.")
            return

    memory["reading_history"].append({
        "url": url,
        "chunks": chunks
    })

    save_memory(memory, filename)
    print("[Memory] Nueva lectura guardada.")


# ==========================================
# 2. RECUPERACIÓN
# ==========================================

def get_reading_history(filename="memory.json"):
    memory = load_memory(filename)
    return memory.get("reading_history", [])


def get_reading_by_url(url, filename="memory.json"):
    history = get_reading_history(filename)

    for reading in history:
        if reading["url"] == url:
            return reading

    return None


# ==========================================
# 3. BÚSQUEDA POR RELEVANCIA
# ==========================================


def search_memory(query, filename="memory.json"):
    history = get_reading_history(filename)
    results = []

    normalized_query = normalize_text(query)
    terms = normalized_query.split()

    for reading in history:
        for chunk in reading["chunks"]:
            normalized_chunk = normalize_text(chunk)
            score = 0

            for term in terms:
                if term in normalized_chunk:
                    score += 1

            if score > 0:
                results.append({
                    "url": reading["url"],
                    "content": chunk,
                    "score": score
                })

    results.sort(
        key=lambda result: result["score"],
        reverse=True
    )

    return results


# ==========================================
# 4. PRUEBAS
# ==========================================

if __name__ == "__main__":

    recovered = load_memory()

    print("Información recuperada:")
    print(recovered)

    history = get_reading_history()

    print("\nHistorial de lecturas:")
    print(f"Total de lecturas: {len(history)}")

    for i, reading in enumerate(history, start=1):
        print(f"\nLectura {i}:")
        print(f"URL: {reading['url']}")
        print(f"Fragmentos: {len(reading['chunks'])}")

    # Recuperación por URL

    result = get_reading_by_url("https://example.com")

    print("\nPrueba de recuperación por URL:")

    if result:
        print("Página encontrada.")
        print(f"URL: {result['url']}")
        print(f"Contenido: {result['chunks'][0]}")
    else:
        print("Página no encontrada.")

    # Búsqueda por relevancia

    results = search_memory("example domain")

    print("\nBúsqueda por relevancia:")

    if results:
        for i, result in enumerate(results, start=1):
            print(f"\nResultado {i}:")
            print(f"URL: {result['url']}")
            print(f"Puntuación: {result['score']}")
            print(f"Contenido: {result['content']}")
    else:
        print("No se encontraron coincidencias.")
