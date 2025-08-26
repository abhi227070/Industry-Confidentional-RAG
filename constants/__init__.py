# Data Loader Constants
BUCKET_NAME = 'industry-confindential-rag'
FILE_PATH = 'Arrora_Company_Internal_Info.pdf'

# Embedding Constants
EMBEDDING_MODEL_NAME = 'models/gemini-embedding-001'

# Text Splitter Constants
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Vector Store Constants
INDEX_NAME = "arrora-company-internal-info"
DIMENSION = 3072
METRICS = 'cosine'
CLOUD = 'aws'
REGION = "us-east-1"
K = 3
SIMILARITY_TYPE = "similarity"

# RAG Chain Constants
MODEL = 'gemini-1.5-flash'
TEMPERATURE = 0.2

# Application Constants
IMAGE_LINK = "https://r2.erweima.ai/imgcompressed/img/compressed_fc9b7b5884b65c15b7ef8f62913ab520.webp"