# GLOBAL VARIABLES
chat_model = "Mistral"
number_docs = 4 # number of docs to retrieve from vector database and pass into llm context window

###
from langchain_community.vectorstores import Chroma

#from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.embeddings import GPT4AllEmbeddings

#embeddings = OllamaEmbeddings(model=model)
embeddings = GPT4AllEmbeddings()

vectordb = Chroma(persist_directory="./data/vectordb", embedding_function=embeddings)

# similarity search
#question = "Have we worked with any sports companies?"
question = "Have we ever worked with any car companies?"

docs = vectordb.similarity_search(
    question,
    k=number_docs,
    #filter={"project_type":'<a id="_gpvn5o1aa5t4"></a>Strategy projects'}
    )

for doc in docs:
    print(doc.metadata)
