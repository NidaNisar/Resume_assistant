from langchain_community.document_loaders import PyPDFLoader
import os
from pathlib import Path


def data_load(pdf_file):
    all_documents=[]
    pdf_directory=Path(pdf_file)
    pdf_files=list(pdf_directory.glob("**/*.pdf"))
    print(f"{len(pdf_files) } for the processing")
    for pdf in pdf_files:
        try:
            print(f"Processing the {pdf.name}")
            loader=PyPDFLoader(str(pdf))
            documents=loader.load()
            for doc in documents:
                doc.metadata['source_file']=pdf.name
                doc.metadata['file_type']='pdf'
                         
            all_documents.extend(documents)
            return all_documents
                    
        except Exception as e:
             print(f"Error in proceesing the file {e}")
        
