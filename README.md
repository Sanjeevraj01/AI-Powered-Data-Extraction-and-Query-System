# AI-Powered Data Extraction and Query System

## Overview

The AI-Powered Data Extraction and Query System is a Retrieval-Augmented Generation (RAG) application that extracts text from multiple data sources such as websites, PDF documents, and images. The extracted content is processed, converted into vector embeddings, stored in Pinecone, and retrieved using semantic search to generate context-aware responses using NVIDIA NIM.

The application provides a FastAPI backend for data ingestion and querying, along with a Streamlit frontend for an intuitive user experience.

---

# Features

## Data Extraction

### Website Extraction
- Extract textual content from web pages using BeautifulSoup.
- Remove HTML tags and process clean text.

### PDF Extraction
- Extract text from PDF documents using pdfplumber.

### Image OCR
- Extract text from JPG, JPEG, and PNG images using:
  - OpenCV
  - Tesseract OCR

---

## Semantic Search

- Text chunking using LangChain Text Splitter.
- Embedding generation using Pinecone Inference (`llama-text-embed-v2`).
- Semantic vector search using Pinecone.

---

## AI-Powered Question Answering

- Retrieval-Augmented Generation (RAG).
- Context-aware response generation using NVIDIA NIM.
- Similarity-based retrieval from Pinecone.

---

## User Interface

- Streamlit-based frontend.
- URL ingestion.
- PDF upload.
- Image upload.
- AI query interface.

---

# System Architecture


```text
                   ┌───────────────┐
                   │  Streamlit UI │
                   └───────┬───────┘
                           │
                           ▼
                   ┌───────────────┐
                   │    FastAPI    │
                   └───────┬───────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼

      Website             PDF             Image
   (BeautifulSoup)    (pdfplumber)   (OpenCV + OCR)

          │                │                │
          └────────────────┴────────────────┘
                           │
                           ▼

                      Extracted Text
                           │
                           ▼

                        Chunking
                           │
                           ▼

                   llama-text-embed-v2
                           │
                           ▼

                       Pinecone
                           │
                           ▼

                    Similarity Search
                           │
                           ▼

                    Retrieved Chunks
                           │
                           ▼

                       NVIDIA NIM
                           │
                           ▼

                    Generated Answer
```
```

---

# Project Structure

```text
data_extraction_and_query_system/
│
├── backend/
│   │
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── load.py
│   │   ├── query.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── url_extractor.py
│   │   ├── image_extractor.py
│   │   ├── pdf_extractor.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── pinecone_db.py
│   │   ├── llm_service.py
│   │   └── __init__.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── __init__.py
│   │
│   └── models/
│       ├── schemas.py
│       └── __init__.py
│
├── frontend/
│   └── app.py
│
├── uploads/
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# Project Structure

```text
data_extraction_and_query_system/
│
├── backend/
│   │
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── load.py
│   │   ├── query.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── url_extractor.py
│   │   ├── pdf_extractor.py
│   │   ├── image_extractor.py
│   │   ├── chunking.py
│   │   ├── embeddings.py
│   │   ├── pinecone_db.py
│   │   ├── llm_service.py
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── schemas.py
│   │   └── __init__.py
│   │
│   └── config/
│       ├── settings.py
│       └── __init__.py
│
├── frontend/
│   └── app.py
│
├── uploads/
│   └── .gitkeep
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| Vector Database | Pinecone |
| Embedding Model | llama-text-embed-v2 |
| LLM | NVIDIA NIM |
| OCR Engine | Tesseract OCR |
| Image Processing | OpenCV |
| PDF Processing | pdfplumber |
| Web Scraping | BeautifulSoup |
| Chunking | LangChain Text Splitter |

---

# Prerequisites

Before running the project, install the following:

- Python 3.10 or above
- Git
- Tesseract OCR
- Pinecone Account
- NVIDIA Developer Account

---

# Installation

## Step 1: Clone the Repository

```bash
git clone <repository-url>

cd data_extraction_and_query_system
```

---

## Step 2: Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

# Install Tesseract OCR

## Windows

Download:

https://github.com/UB-Mannheim/tesseract/wiki

Install to:

```text
C:\Program Files\Tesseract-OCR\
```

Verify installation:

```bash
tesseract --version
```

---

## Ubuntu/Linux

```bash
sudo apt update

sudo apt install tesseract-ocr
```

Verify installation:

```bash
tesseract --version
```

---

# Configuration

## Environment Variables

Create a `.env` file in the project root directory.

```env
NVIDIA_API_KEY=your_nvidia_api_key

PINECONE_API_KEY=your_pinecone_api_key

PINECONE_INDEX_NAME=data-extraction-index
```

---

# Pinecone Configuration

## Create a Pinecone Index

Login to Pinecone and create an index.

### Recommended Settings

| Setting | Value |
|----------|----------|
| Index Name | data-extraction-index |
| Cloud Provider | AWS |
| Similarity Metric | Cosine |
| Embedding Model | llama-text-embed-v2 |

---

# Running the Application

## Start FastAPI Backend

Navigate to the backend directory:

```bash
cd backend
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## Start Streamlit Frontend

Open a new terminal and run:

```bash
streamlit run frontend/app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# API Endpoints

## Load Data

### Endpoint

```http
POST /load
```

### Supported Inputs

#### URL

```json
{
  "source_type": "url",
  "url": "https://example.com"
}
```

#### PDF Upload

```text
source_type=file
file=document.pdf
```

#### Image Upload

```text
source_type=image
file=image.jpg
```

### Functionality

- Extract content.
- Split into chunks.
- Generate embeddings.
- Store vectors in Pinecone.

---

## Query Data

### Endpoint

```http
POST /query
```

### Request

```json
{
  "query": "What is the leave policy?"
}
```

### Response

```json
{
  "answer": "Generated response from NVIDIA NIM."
}
```

---

# Application Workflow

## URL Processing

```text
Website URL
      │
      ▼
BeautifulSoup
      │
      ▼
Extracted Text
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Pinecone
```

---

## PDF Processing

```text
PDF Document
      │
      ▼
pdfplumber
      │
      ▼
Extracted Text
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Pinecone
```

---

## Image Processing

```text
Image
      │
      ▼
OpenCV
      │
      ▼
Tesseract OCR
      │
      ▼
Extracted Text
      │
      ▼
Chunking
      │
      ▼
Embeddings
      │
      ▼
Pinecone
```

---

## Query Workflow

```text
User Query
      │
      ▼
Generate Query Embedding
      │
      ▼
Pinecone Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
NVIDIA NIM
      │
      ▼
Generated Answer
```

---

# Usage Guide

## Uploading a Website URL

1. Open the Streamlit application.
2. Select the URL option.
3. Enter a valid website URL.
4. Click Load URL.
5. Wait for indexing completion.

---

## Uploading a PDF

1. Select PDF Upload.
2. Upload a PDF document.
3. Click Process PDF.
4. Wait for extraction and indexing.

---

## Uploading an Image

Supported formats:

- JPG
- JPEG
- PNG

Steps:

1. Select Image Upload.
2. Upload an image.
3. Click Process Image.
4. OCR extracts text.
5. Text is indexed into Pinecone.

---

## Asking Questions

1. Ensure data has been indexed.
2. Enter a question.
3. Click Get Answer.
4. Review the generated response.

---

# Error Handling

The application handles:

- Invalid URLs
- Unsupported file types
- Empty PDF documents
- OCR extraction failures
- Missing environment variables
- Pinecone connection failures
- NVIDIA NIM API errors

---

# Troubleshooting

## Pinecone Module Not Found

```bash
pip install pinecone
```

---

## Streamlit Module Not Found

```bash
pip install streamlit
```

---

## FastAPI Module Not Found

```bash
pip install fastapi uvicorn
```

---

## Tesseract Not Found

Add the Tesseract executable path:

```python
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

---

# Security Best Practices

- Never commit `.env` files to GitHub.
- Store API keys in environment variables.
- Use `.gitignore` to exclude sensitive files.
- Restrict API access in production environments.

---

# Future Enhancements

- User Authentication
- Conversation Memory
- Source Citations
- Docker Deployment
- AWS EC2 Deployment
- Hybrid Search (Keyword + Vector Search)
- LangSmith Monitoring
- LangGraph Workflows
- Multi-user Support

---
# Conclusion

This project demonstrates a complete end-to-end Retrieval-Augmented Generation (RAG) system capable of extracting information from websites, PDF documents, and images. The solution combines OCR, web scraping, vector search, and large language models to deliver accurate, context-aware responses through an intuitive user interface.