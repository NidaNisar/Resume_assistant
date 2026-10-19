from src.resume_assistant.data_loader import data_load
from src.resume_assistant.chunking import document_splitter


if __name__ == "__main__":

    document = data_load("data")
    chunks = document_splitter(document)