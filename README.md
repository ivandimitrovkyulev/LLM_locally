LLM Locally
=======
### version v0.1.0

-------
### Installation


This project uses **[Python 3.11](https://www.python.org/downloads/)**, **[Poetry](https://python-poetry.org/docs/#installation)**,
**[ollama](https://github.com/ollama/ollama)**

##### 1. Install dependencies

Activate virtual environment and install all third-party project dependencies:
```shell
# Sets Poetry configuration so it creates a virtual environment inside project root folder
poetry config --local virtualenvs.in-project true

# Create a virtual environment
poetry shell

# Install all project dependencies
poetry install
```

##### 2. Install **[ollama](https://github.com/ollama/ollama)** depending on what platform you use.

