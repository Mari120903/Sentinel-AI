
# Sentinel AI

**Version:** 0.1  
**Status:** In Development  
**Language:** Python 3.13

## Description

Sentinel AI is an experimental Python project designed to retrieve, process, and store information from web pages.

The project uses a modular architecture to separate connectivity, content extraction, text processing, and data persistence.

## Current Features

- HTTP connectivity testing.
- Web page content extraction using Requests and BeautifulSoup.
- Text cleaning and normalization.
- Text segmentation into chunks with configurable overlap.
- JSON-based information storage and retrieval.
- Reading history tracking.

## Project Structure

```text
Sentinel AI/
│
├── main.py
├── search.py
├── reader.py
├── processor.py
├── memory.py
├── models.py
├── memory.json
├── requirements.txt
└── README.md
```

## Technologies

- Python
- Requests
- BeautifulSoup
- JSON

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Enter the project directory:

```bash
cd "Sentinel AI"
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Development Roadmap

- [x] HTTP connectivity testing.
- [x] Web content extraction.
- [x] Text processing and segmentation.
- [x] JSON-based persistence.
- [ ] Duplicate URL detection.
- [ ] Semantic memory.
- [ ] Information retrieval.
- [ ] Integration of machine learning models.

## Disclaimer

Sentinel AI is an educational and experimental project. It is not yet an autonomous artificial intelligence system.
