from src.resume_assistant.data_loader import data_load
from src.resume_assistant.chunking import document_splitter
from src.resume_assistant.Embeddings import Embedding_manager


if __name__ == "__main__":

    document = data_load("data")
    chunks = document_splitter(document)
    embedding_model = Embedding_manager()
    
    texts = [doc.page_content for doc in chunks]
    
    embeddings = embedding_model.generate_embedding(texts)