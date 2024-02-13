
import os
import shutil

from langchain.document_loaders import NotionDirectoryLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma


# Read the content of a markdown file
with open("data/raw/projects.md", "r") as file:
    markdown_doc = file.read()

# Define the headers to split on
headers_to_split_on = [
    ("#", "project_type"),  # Split on '#' for project_type
    ("##", "client_name"),  # Split on '##' for client_name
]

# Split the markdown text based on the defined headers
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)
md_header_splits = markdown_splitter.split_text(markdown_doc)

# Embed content and save to vector database
embeddings = OllamaEmbeddings(model="phi")

# Remove old database files if any
vector_db_path = './data/vectordb/'
if os.path.exists(vector_db_path):
    shutil.rmtree(vector_db_path)
    os.mkdir(vector_db_path)
else:
    os.mkdir(vector_db_path)

# Create a new vector database
vectordb = Chroma.from_documents(
    documents=md_header_splits,
    embedding=embeddings,
    persist_directory=vector_db_path
)

print(f"Created vector database with {vectordb._collection.count()} documents")
