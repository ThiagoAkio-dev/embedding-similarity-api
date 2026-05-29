from src.document_reader import DocumentReader
from src.embedding_service import EmbeddingService
from src.similarity_service import SimilarityService

def main():

    
    document_reader = DocumentReader("document.txt")
    embedding_service = EmbeddingService()
    similarity_service = SimilarityService() 

    try: 
        
        document_text = document_reader.read_text()

        user_text = input ("Can you guess the phrase? Type a phrase to compare: ")


        
        document_embedding = embedding_service.generate_embedding(document_text)
        user_embedding = embedding_service.generate_embedding(user_text)


        
        similarity = similarity_service.cosine_similarity(
            document_embedding,
            user_embedding
        )

        
        percentage = similarity_service.to_percentage(similarity)


        print("\n --- Similarity Percentage ---")
        print(f"Similarity: {percentage:.2f}%")


    except FileNotFoundError:
        print("File not found")
    
if __name__ == "__main__":
    main()


