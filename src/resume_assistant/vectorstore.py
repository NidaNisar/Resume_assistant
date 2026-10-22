import chromadb
from chromadb import PersistentClient
import os
import uuid
from typing import List
class Vectorstore:
    def __init__(self,collection_name='resume_document',persistant_directory:str='../vectorstore'):
        self.collection_name=collection_name
        self.persistant_directory=persistant_directory
        self.client=None,
        self.collection=None
        self._initialize_store()
    def _initialize_store(self):
        try:
             os.makedirs(self.persistant_directory,exist_ok=True)
             self.client=chromadb.PersistentClient(self.persistant_directory)
             self.collection=self.client.get_or_create_collection(
             name=self.collection_name,
              metadata={"hnsw:space": "cosine"}
             )
             print(f"Vector store initialize {self.collection}")
             print(f"Existing document in the store {self.collection.count()}")
        except Exception as e:
            print(f"Error in collection {e}")
    def add_documents(self,documents:List[str],embeddings):
                    if len(documents)!=len(embeddings):
                        return ValueError("length of document and embeddings does not match")
                    
                   
                        #Prepare data for store in the choromadb
                    ids=[]
                    metadatas=[]
                    embedding=[]
                    document=[]
                    for i,(doc,embedd) in enumerate(zip(documents,embeddings)):
                            #id 
                        doc_id=f"doc_{uuid.uuid4().hex[:8]}_{i}"
                        ids.append(doc_id)
                            # metadata
                        document.append(doc.page_content)
                        embedding.append(embedd.tolist())
                        metadata=dict(doc.metadata)
                        metadata['index']=i
                        metadata['content_length']=len(doc.page_content)
                        metadatas.append(metadata)
                  
                    try:
                        exist=self.collection.get(
                             ids=[doc_id]
                         )
                        if exist:
                            print("Duplicate — skipping")
                        else:    
                         self.collection.add(ids=ids,
                         metadatas=metadatas,
                         embeddings=embedding,
                         documents=document )
                        print(f" successfully Add the {len(documents)} document to the vector db")
                        print(f"Total {(self.collection.count())} documents in the vecttore db")
            
                           
                    except Exception as e:
                         print(f"Error in collection {e}")
                
            
            
                       
                    
                   
            
                   
            
                                               