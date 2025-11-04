from .vector_store import VectorDB
from .embedding import EmbeddingModel

class Retriever:
    """
    Provides a retriever interface for querying the vector database.
    """
    def __init__(self):
        """
        Initializes the Retriever by creating an embedding model and a vector database instance.
        """
        embedding = EmbeddingModel()
        embedding_model = embedding.get_embedding_model()
        self.vectorstore = VectorDB(embedding_model)

    def get_retriever(self):
        """
        Returns a retriever object from the vector store for similarity search.
        Returns:
            Retriever: The retriever object for querying documents.
        """
        return self.vectorstore.get_retriever()