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