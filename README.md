# Sprints & Snekers Demo API

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Een eenvoudige maar krachtige API demo gemaakt voor de sollicitatie bij Sprints & Sneakers. Deze API toont mijn vaardigheden in het bouwen van efficiënte en schaalbare backend oplossingen met FastAPI.

## 🚀 Functies

- Real-time begroeting speciaal voor Sharif
- Eenvoudige en intuïtieve API endpoint
- Snelle response tijden dankzij FastAPI's asynchrone verwerking
- Nette en gestructureerde code volgens Python best practices

## 🛠️ Technische Stack

- **Python 3.8+** - Programmeertaal
- **FastAPI** - Moderne, snelle web framework
- **Uvicorn** - ASGI server voor productiegebruik

## ⚡ Snel aan de slag

### Vereisten

- Python 3.8 of hoger
- pip (Python package manager)

### Installatie

1. Kloon de repository:
   ```bash
   git clone [repository-url]
   cd S&S
   ```

2. Installeer de benodigde packages:
   ```bash
   pip install -r requirements.txt
   ```

### Gebruik

Start de applicatie met:
```bash
uvicorn main:app --reload
```

Bezoek vervolgens in je browser:
```
http://127.0.0.1:8000/hello
```

Of test de API met curl:
```bash
curl http://127.0.0.1:8000/hello
```

## 📚 API Documentatie

Wanneer de applicatie draait, is de interactieve API documentatie beschikbaar op:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 📄 Licentie

Geen licentie voor de demo.