from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from constants import EMBEDDING_MODEL_NAME

class EmbeddingModel:
    """
    Handles the initialization and retrieval of the Google Generative AI Embedding model.
    """
    def __init__(self):
        """
        Loads the Google API key from environment variables.
        """
        load_dotenv()
        self._GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    def get_embedding_model(self):
        """
        Returns an instance of the GoogleGenerativeAIEmbeddings model.
        Returns:
            GoogleGenerativeAIEmbeddings: The embedding model instance.
        """
        model = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL_NAME)
        return model