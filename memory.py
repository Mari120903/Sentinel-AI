
import json
import os


def save_memory(data, filename="memory.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_memory(filename="memory.json"):
    if not os.path.exists(filename):
        return {}

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def get_reading_history(filename="memory.json"):
    memory = load_memory(filename)
    return memory.get("reading_history", [])


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
