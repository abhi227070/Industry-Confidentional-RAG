# Aurora Industry Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for industry document Q&A, built with Streamlit, LangChain, and Pinecone.

## Features
- Uploads and processes PDF documents from AWS S3
- Splits documents and generates embeddings
- Stores and retrieves vectors using Pinecone
- Uses Google Generative AI for answering queries
- User-friendly Streamlit web interface

## Getting Started

### Prerequisites
- Docker (recommended) or Python 3.10+
- AWS, Pinecone, and Google API credentials

### Environment Variables
Create a `.env` file in the project root with the following (example):
```
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
REGION=your_aws_region
BUCKET_NAME=your_s3_bucket
FILE_PATH=your_pdf_file_path
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
INDEX_NAME=your_pinecone_index
DIMENSION=your_embedding_dimension
METRICS=cosine
CLOUD=aws
REGION=your_pinecone_region
MODEL=your_generative_model
TEMPERATURE=0.2
EMBEDDING_MODEL_NAME=your_embedding_model
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
K=5
SIMILARITY_TYPE=similarity
```

### Build & Run with Docker
```sh
docker build -t aurora-chatbot .
docker run -p 8501:8501 --env-file .env aurora-chatbot
```

### Run Locally (without Docker)
```sh
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure
- `app.py` - Streamlit UI
- `components/` - Data loading, embedding, vector store, etc.
- `pipeline/` - RAG chain logic
- `constants/` - Configuration constants

## License
MIT
