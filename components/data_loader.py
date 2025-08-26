import os
import boto3
from io import BytesIO
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_core.documents import Document
from constants import BUCKET_NAME, FILE_PATH

load_dotenv()

class DataLoader:
    """
    Loads PDF data from an AWS S3 bucket and returns a list of LangChain Document objects.
    """
    def __init__(self):
        """
        Initializes the DataLoader by loading AWS credentials from environment variables.
        """
        load_dotenv()
        self._AWS_REGION = os.getenv('REGION')
        self._AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
        self._AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

    def get_data(self):
        """
        Downloads a PDF file from S3, reads its pages, and returns a list of Document objects.
        Returns:
            list[Document]: List of documents, one per non-empty PDF page.
        """
        # Create S3 client using credentials
        s3 = boto3.client(
            's3',
            aws_access_key_id=self._AWS_ACCESS_KEY,
            aws_secret_access_key=self._AWS_SECRET_KEY,
            region_name=self._AWS_REGION
        )

        bucket_name = BUCKET_NAME
        key = FILE_PATH

        # Get PDF file from S3 into memory
        pdf_obj = s3.get_object(Bucket=bucket_name, Key=key)
        pdf_bytes = pdf_obj['Body'].read()
        pdf_stream = BytesIO(pdf_bytes)

        # Read PDF directly from memory
        reader = PdfReader(pdf_stream)
        docs = []

        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:  # avoid empty pages
                docs.append(Document(page_content=text, metadata={"page": page_num + 1}))

        return docs