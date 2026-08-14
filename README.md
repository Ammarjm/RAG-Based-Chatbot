# RAG-Based Chatbot

A simple AI chatbot built using Retrieval-Augmented Generation (RAG).

The chatbot answers questions based on a custom knowledge base about Al-Balqa Applied University and the Faculty of Artificial Intelligence.

## Features

- Loads information from a text document
- Splits the document into smaller chunks
- Creates embeddings using HuggingFace
- Stores embeddings using FAISS
- Retrieves relevant information based on the user's question
- Sends the retrieved context to an LLM
- Generates answers based on the provided knowledge base

## Technologies Used

- Python
- LangChain
- HuggingFace Embeddings
- FAISS
- OpenRouter API

## Project Files

- `app.py` - Runs the chatbot
- `RAG.py` - Handles document loading, chunking, embeddings, and retrieval
- `llm_model.py` - Configures the language model
- `prompts.py` - Contains the RAG prompt
- `balqa_ai.txt` - Knowledge base used by the chatbot

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
