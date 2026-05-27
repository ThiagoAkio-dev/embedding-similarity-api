def main():

    ## Have to finish those class later
    document_reader = DocumentReader("document.txt")
    embedding_service = EmbeddingService()
    similarity_service = SimilarityService() 

    try: 
        ### Do this Method to read the txt on the document.txt
        document_text = document_reader.read_text()

        user_text = input ("Can you guess the phrase? Type a phrase to compare: ")


        ### Do these methods to generate the embedding s of the the document and the user text 
        document_embedding = embedding_service.generate_embedding(document_text)
        user_embedding = embedding_service.generate_embedding(user_text)


        ### Finish this method to calculate the simjilarity of both the user text and the document text
        similarity = similarity_service.cosine_similarity(
            document_embedding,
            user_embedding
        )

        ### Show the simjilarity in percentage
        percentage = similarity_service.to_percentage(similarity)


        print("\n --- Similarity Percentage ---")
        print(f"Similarity: {percentage:.2f}%")


    except FileNotFoundError:
        print("File not found")
    
if __name__ == "__main__":
    main()


