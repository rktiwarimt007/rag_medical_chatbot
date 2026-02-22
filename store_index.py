from dotenv import load_dotenv
import os

from src.helper import load_pdfs_files, filter_to_minimal_docs, split_documents, download_embeddings_model
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

extracted_docs = load_pdfs_files("data/")
filtered_docs = filter_to_minimal_docs(extracted_docs)
split_docs = split_documents(filtered_docs) 

embeddings_model = download_embeddings_model("sentence-transformers/all-MiniLM-L6-v2")

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,  # Dimension of the embeddings
        metric="cosine",  # Similarity metric
        spec=ServerlessSpec(cloud="aws", region="us-east-1")  # Serverless configuration
    )
    
index = pc.Index(index_name)


docsearch = PineconeVectorStore.from_documents(
        documents=split_docs,
        embedding=embeddings_model,
        index_name=index_name
)