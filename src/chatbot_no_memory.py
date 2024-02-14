#%%
# GLOBAL VARIABLES
chat_model = "Mistral"
number_docs = 4 # number of docs to retrieve from vector database and pass into llm context window

###
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Load vector database
embeddings = GPT4AllEmbeddings()
vectordb = Chroma(persist_directory="./data/vectordb", embedding_function=embeddings)
retriever=vectordb.as_retriever(k=number_docs)

# Define LLM
llm = ChatOllama(model=chat_model)

# Build prompt
template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Keep the answer as concise as possible.
<context>
{context}
</context>
Question: {question}
Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# Run chain
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    #chain_type="map_reduce"
    #chain_type="refine"
)

#question = "Have we ever worked with any car companies?"
question = "Have we ever worked with any companies that produce cars?"

result = qa_chain({"query": question})
result["result"]
#result["source_documents"][0]


# %%
