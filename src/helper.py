from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document
from langchain_community.embeddings import HuggingFaceEmbeddings




# Extracting text from PDF files
def load_pdfs_files(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader, show_progress=True)
    documents = loader.load()
    return documents

# Filter the documents to only include the page content and source metadata
def filter_to_minimal_docs(documents: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in documents:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
        
    return minimal_docs


# Split the documents into smaller chunks

def split_documents(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=20,
    )
    chunks = text_splitter.split_documents(minimal_docs)
    return chunks


# Downlaod the Embedding model from HuggingFace
def download_embeddings_model(model_name):
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings 