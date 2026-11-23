import requests


def test_connection():
    print("\n[Search] Intentando conectar a Internet...")

    url = "https://example.com"

    response = requests.get(url)

    print(f"Estado HTTP: {response.status_code}")

    if response.status_code == 200:
        print("✅ Conexión exitosa.")
        print(f"La página tiene {len(response.text)} caracteres.")
    else:
        print("❌ No se pudo acceder a la página.")