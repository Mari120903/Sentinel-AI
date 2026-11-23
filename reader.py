import requests
from bs4 import BeautifulSoup

def read_page(url):
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text(separator=" ", strip=True)

    return None

if __name__ == "__main__":
    content = read_page("https://example.com")
    print(content)