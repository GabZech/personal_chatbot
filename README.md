# personal_chatbot

## Getting started

### Requirements

- Python 3.9
- [Ollama](https://ollama.com/) for running local models

### Installation

1. cd to the project folder
2. run `pipenv install` to install all dependencies from the Pipfile
    - If you don't have pipenv install, run `pip install pipenv`
3. Put your Markdown files under `data/raw`
4. Pull your LLM from Ollama, e.g. `ollama run mistral`

### Usage

- For simple retrieval, edit the desired search question under [src/retrieval.py](src/retrieval.py) and run it in your IDE.
- To pass those documents into the context window of an LLM and generate an answer, edit and run [src/chatbot.py](src/chatbot.py)