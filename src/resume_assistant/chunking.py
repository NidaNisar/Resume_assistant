from langchain_text_splitters import RecursiveCharacterTextSplitter


def document_splitter(document,chunk_size=1000,chunk_overlap=200):
    print(f"Before splitting {len(document)}")
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n","\n"," ",""])
    split_document=text_splitter.split_documents(document)
    
    if split_document:
        print(f"total {len(split_document)} chunks for {len(document)} document ")
        print("Example of chunk")
        print(f"Page Content {split_document[1].page_content[:200]}")
        print(f"Split documents {split_document}")

    return split_document
    

