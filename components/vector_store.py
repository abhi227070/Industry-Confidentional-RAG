from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv
from constants import *

class VectorDB:
    """
    Handles the creation and management of the Pinecone vector database for document storage and retrieval.
    """
    def __init__(self, embedding_model):
        """
        Initializes the Pinecone vector database and creates the index if it does not exist.
        Args:
            embedding_model: The embedding model to use for vectorization.
        """
        load_dotenv()
        pinecone_api_key = os.environ.get("PINECONE_API_KEY")
        pc = Pinecone(api_key=pinecone_api_key)

        # Create the index if it doesn't exist
        if not pc.has_index(INDEX_NAME):
            pc.create_index(
                name=INDEX_NAME,
                dimension=DIMENSION,
                metric=METRICS,
                spec=ServerlessSpec(cloud=CLOUD, region=REGION),
            )

        index = pc.Index(INDEX_NAME)

        # Initialize Pinecone Vector Store
        self.vector_store = PineconeVectorStore(
            index=index,
            embedding=embedding_model
        )

    def add_document(self, docs):
        """
        Adds a list of documents to the vector store.
        Args:
            docs (list): List of Document objects to add.
        """
        self.vector_store.add_documents(docs)

    def get_retriever(self):
        """
        Returns a retriever object for similarity search from the vector store.
        Returns:
            Retriever: The retriever object for querying documents.
        """
        return self.vector_store.as_retriever(search_kwargs={'k': K}, search_type=SIMILARITY_TYPE)