from langchain.text_splitter import RecursiveCharacterTextSplitter
from constants import CHUNK_OVERLAP, CHUNK_SIZE

class TextSplitter:
    """
    Splits documents into smaller chunks using recursive character splitting.
    """
    def __init__(self):
        """
        Initializes the text splitter with specified chunk size and overlap.
        """
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

    def split_data(self, docs):
        """
        Splits the input documents into smaller chunks.
        Args:
            docs (list): List of Document objects to split.
        Returns:
            list: List of splitted Document objects.
        """
        splitted_docs = self.splitter.split_documents(docs)
        return splitted_docs