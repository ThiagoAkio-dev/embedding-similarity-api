from sentence_transformers import SentenceTransformer

class EmbeddingService:

    def __init__(self, model_name: str = "paraphrase-multilingual-MiniLM-L12-v2"):
        self.model = SentenceTransformer(model_name)


    def generate_embedding(self, text: str):

        if not text.strip():
            raise ValueError("Text cannot be empty")
        
        return self.model.encode(text)
    