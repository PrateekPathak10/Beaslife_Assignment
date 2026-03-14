# Beastlife AI Automation & Customer Intelligence System

### Link: https://prateekpathakbeastlifeassignment.streamlit.app/

## Overview

This project implements an AI-powered customer support automation system that automatically categorizes customer queries, generates responses using Retrieval-Augmented Generation (RAG), and visualizes insights through a dashboard.

The system helps companies understand the most common customer issues and automate responses to reduce support workload.

---

## Features

- AI-based customer query classification
- Retrieval-Augmented Generation (RAG) for automated responses
- Vector database for knowledge retrieval
- Real-time API for processing queries
- Analytics dashboard for customer support insights
- AI chatbot interface for testing support automation

---

## System Architecture

```
Customer Query
      ↓
FastAPI Endpoint
      ↓
LangChain Query Classification
      ↓
FAISS Vector Database (FAQ Retrieval)
      ↓
Local LLM (Llama3 via Ollama)
      ↓
Automated Response Generation
      ↓
Store Query in Dataset
      ↓
Streamlit Dashboard Visualization
```

---

## AI Query Categories

The system classifies queries into the following categories:

- Order Status
- Delivery Delay
- Refund Request
- Product Issue
- Payment Problem
- Subscription Issue
- General Query

---

## Technologies Used

### AI & NLP
- LangChain
- Llama3 (Ollama local LLM)
- Sentence Transformers
- FAISS Vector Database

### Backend
- FastAPI
- Python

### Data Processing
- Pandas

### Dashboard
- Streamlit
- Plotly

---

## Project Structure

```
beastlife_assignment/

api.py                # FastAPI endpoint
app.py                # Streamlit dashboard
classifier.py         # Query classification logic
rag_engine.py         # RAG response generation
vector_store.py       # FAISS vector database creation
dataset.csv           # Query dataset
faq_data.txt          # Knowledge base
requirements.txt      # Dependencies
```

---

## How It Works

1. Customer queries are received through the FastAPI endpoint.
2. LangChain uses an LLM to classify the query into issue categories.
3. The system retrieves relevant FAQ information from a FAISS vector database.
4. The LLM generates an automated response using RAG.
5. Query data is stored in a dataset for analytics.
6. A Streamlit dashboard visualizes insights like issue distribution and trends.

---

## Dashboard Insights

The dashboard displays:

- Total number of queries
- Issue distribution across categories
- Query trends over time
- Recent customer queries
- AI customer support assistant chatbot

---

## Example Query

Input:

```
My order hasn't arrived yet
```

Output:

```
Category: Delivery Delay
Response: Delivery usually takes 3-5 business days.
```

---

## Scalability

The system can scale using:

- Message queue systems (Kafka/RabbitMQ)
- Microservices architecture
- Cloud deployment (AWS/GCP/Azure)
- Distributed LLM inference
- Optimized vector database search

---

## Author

Prateek Pathak
