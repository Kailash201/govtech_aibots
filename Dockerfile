# Use an official Python image as the base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install libreoffice (for pdf parsing), tesseract for ocr
RUN apt-get update && apt-get install -y \
    libreoffice\
    tesseract-ocr \
    libtesseract-dev \
    poppler-utils

# Copy only the requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install python-multipart
RUN pip install pytest httpx
RUN pip install -U duckduckgo-search
RUN pip install arxiv
RUN pip install xmltodict
RUN pip install wikipedia
RUN pip install langchain_community
RUN pip install langchain
RUN pip install beanie
RUN pip install 'fastapi[standard]'
RUN pip install python-dotenv
RUN pip install langchain_openai
RUN pip install langgraph
RUN pip install unstructured
RUN pip install tiktoken
RUN pip install docx
RUN pip install 'unstructured[docx,pptx,pdf,doc,ppt,xlsx]'

# Copy the entire application
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Run the application
CMD ["fastapi", "run", "src/th_assign/main.py" ,"--host", "0.0.0.0", "--port", "8000"]