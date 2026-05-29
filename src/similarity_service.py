import numpy as np
class SimilarityService:
    
    ### Implement Method cosine_similarity
    @staticmethod
    def cosine_similarity(embedding1, embedding2) -> float:

        embedding1 = np.array(embedding1)
        embedding2 = np.array(embedding2)

        dot_product = np.dot(embedding1, embedding2)
        norm1 = np.linalg.norm(embedding1)
        norm2 = np.linalg.norm(embedding2)

        if norm1 == 0 or norm2 == 0:
            raise ValueError("Not possible to calculate a similarity with a null vector")
        
        similarity = dot_product / (norm1 * norm2)

        return float(similarity)

    @staticmethod
    def to_percentage(similarity: float) -> float:
        return similarity * 100