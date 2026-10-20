from sentence_transformers import SentenceTransformer
from typing import List
class Embedding_manager:
    def __init__(self,model_name:str='all-MiniLM-L6-v2'):
       self.model_name=model_name
       self.model=None
       self._loader_()
    def _loader_(self):
        print(f"Load model for emdedding {self.model_name}")
        self.model=SentenceTransformer(self.model_name)
        print(f"Embedding shape for the model {self.model.get_embedding_dimension()}")
    def generate_embedding(self,text=List[str]):
        try:
            print(f"Sucessfully loaded the model {self.model}")
            print(f"total {len(text)} chunks for embedding")
            embeddings_txt=self.model.encode(text)
            print(f"after embedding total chunks {len(embeddings_txt)}")
           

            return embeddings_txt
        except Exception as e:
            print(f"Error in embeddings {e}")
        
