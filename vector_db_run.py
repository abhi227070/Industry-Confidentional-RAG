
# Import necessary components for data loading, splitting, embedding, and vector storage
from components.data_loader import DataLoader
from components.text_splitter import TextSplitter
from components.embedding import EmbeddingModel
from components.vector_store import VectorDB


# Initialize the data loader and load the raw documents
data_loader = DataLoader()
docs = data_loader.get_data()

# Initialize the text splitter and split the documents into smaller chunks
splitter = TextSplitter()
splitted_docs = splitter.split_data(docs)

# Initialize the embedding model and get the embedding function/model
embedding = EmbeddingModel()
embedding_model = embedding.get_embedding_model()

# Initialize the vector database with the embedding model and add the splitted documents
vectordb = VectorDB(embedding_model=embedding_model)
vectordb.add_document(splitted_docs)