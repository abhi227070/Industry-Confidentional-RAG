# Use the official Python image as a base
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose Streamlit default port
EXPOSE 8501

# Set Streamlit environment variables for better container experience
ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ENABLECORS=false

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
