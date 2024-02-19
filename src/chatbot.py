# GLOBAL VARIABLES

question = "Have we worked with any sports companies?"
#question = "Did we ever have a sustainability use case or project?"
#question = "What clients have we worked in the manufacturing industry?"


chat_model = "Mistral"
number_docs = 4 # number of docs to retrieve from vector database and pass into llm context window
chain_type = None # None or "map_reduce" or "refine"
temperature = 1.0

'''
CHAIN OPTIONS
- [chain_type = None] uses a basic retrieval QA with all k documents passed into the context window
- [chain_type = "map_reduce"] uses a map reduce QA chain
- [chain_type = "refine"] uses a refine QA chain
'''

###################################################################################
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def load_db(number_docs):

    # Load vector database
    embeddings = GPT4AllEmbeddings()
    vectordb = Chroma(persist_directory="./data/vectordb", embedding_function=embeddings)
    retriever = vectordb.as_retriever(k=number_docs)

    return vectordb, retriever


def load_chain(retriever, chat_model, temperature,  chain_type=None):

    # Define LLM
    llm = ChatOllama(model=chat_model,
                     temperature=temperature
                     )

    # Build prompt
    template = """

    You are an assistant for question-answering tasks about client projects of a consulting firm. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

    Context: {context}
    Question: {question}

    Answer:
    """
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    # Run chain
    if chain_type is None:
        qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        )
    else:
        qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=retriever,
            return_source_documents=True,
            chain_type=chain_type,
        )

    return qa_chain

def run_chain(qa_chain, question):

    result = qa_chain({"query": question})
    #result["source_documents"][0]

    return result

vectordb, retriever = load_db(number_docs)
qa_chain = load_chain(retriever, chat_model, temperature, chain_type)
response = run_chain(qa_chain, question)

# print results

print("\n\n ### ANSWER ### \n")
print(response["result"])

print("\n ### SOURCE DOCUMENTS ### \n")
for doc in response["source_documents"]:

    try:
        print(f"Client name: {doc.metadata['client_name']}\nProject type: {doc.metadata['project_type']}\n")
    except:
        print("No client name or project type in metadata \n")

