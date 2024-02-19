# personal_chatbot

## Getting started

### Requirements

- Python 3.9
- [Ollama](https://ollama.com/) for running local models

### Installation

1. cd to the project folder
2. run `pipenv install` to install all dependencies from the Pipfile
    - If you don't have pipenv install, run `pip install pipenv`
3. Pull your LLM from Ollama, e.g. `ollama run mistral`

### Usage

- First, put your Markdown file under `data/raw` and create your vector database using [src/create_vectordb.py](src/create_vectordb.py)
- For simple retrieval, edit the desired search question under [src/retrieval.py](src/retrieval.py) and run it in your IDE.
- To pass those documents into the context window of an LLM and generate an answer, edit and run [src/chatbot.py](src/chatbot.py)