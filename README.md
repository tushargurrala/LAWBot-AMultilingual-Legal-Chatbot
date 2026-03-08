# LAWBot – Multilingual Legal Rights Chatbot for Rural India

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-FF4B4B.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green.svg)](https://langchain.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

LAWBot is an AI-powered multilingual legal assistant designed to help rural citizens understand Indian laws, rights, and legal procedures.

The system uses Retrieval-Augmented Generation (RAG) technology to retrieve relevant information from legal documents and generate accurate responses.

Users can ask legal questions using **text or voice** and receive answers in their **native language**.

---

## Key Features

- **Multilingual Support** – Supports English, Hindi, Telugu, Tamil, Kannada, Malayalam, Marathi, Bengali, Gujarati, and Punjabi.
- **Voice Assistant** – Users can speak their legal questions and listen to the chatbot's answers.
- **AI-Powered Legal Q&A** – Provides information related to Indian laws, rights, and legal procedures.
- **RAG-Based Knowledge Retrieval** – Retrieves relevant legal information from official legal documents.
- **Quick Legal Questions** – Provides quick access buttons for common legal queries.
- **Emergency Legal Help** – Displays important helpline numbers like police, ambulance, women helpline, and legal aid.
- **Clean User Interface** – Simple and responsive interface built using Streamlit.

---

## Use Cases

LAWBot can assist users with:

- Understanding fundamental rights
- Learning about IPC sections
- Filing FIR complaints
- Property registration guidance
- Consumer protection information
- Women protection laws
- Legal awareness for rural citizens

---

## Technical Architecture


User Query
    ↓
Streamlit Web Interface
    ↓
Speech / Text Processing
    ↓
Language Translation
    ↓
LangChain RAG Pipeline
    ↓
Vector Database (ChromaDB)
    ↓
Semantic Search
    ↓
Legal Context Retrieval
    ↓
AI Response Generation
    ↓
Text + Voice Output


---

## Technology Stack

Frontend  
Streamlit

Programming Language  
Python

AI Framework  
LangChain

Vector Database  
ChromaDB

Embeddings  
HuggingFace Sentence Transformers

Translation  
Deep Translator

Speech Processing  
SpeechRecognition  
gTTS (Google Text-to-Speech)

---

## Prerequisites

- Python 3.10 or higher  
- Windows / Linux / MacOS  
- Internet connection  
- Minimum 4GB RAM recommended  

---

## Installation and Setup

### 1 Clone the Repository


git clone https://github.com/ThusharGurrala/LAWBot-AMultilingual-Legal-Chatbot.git

cd LAWBot-AMultilingual-Legal-Chatbot


---

### 2 Create Virtual Environment

Windows


python -m venv venv
venv\Scripts\activate


Linux / Mac


python3 -m venv venv
source venv/bin/activate


---

### 3 Install Dependencies


pip install -r requirements.txt


---

### 4 Create Vector Embeddings


python create_embeddings.py


This step processes legal documents and creates a searchable vector database.

---

### 5 Run the Application


streamlit run app.py


Open the application in your browser:


http://localhost:8501


---

## Project Structure


LAWBot/
│
├── app.py
├── lawbot_engine.py
├── create_embeddings.py
├── requirements.txt
├── .env
├── .gitignore
│
├── data/
│ ├── Constitution of India.pdf
│ ├── Indian Penal Code.pdf
│ ├── Indian Contract Act.pdf
│ └── Indian Evidence Act.pdf
│
└── legal_vector_store/


---

## Example Queries

English


How to file FIR in India?
What are fundamental rights?
How to register property in India?


Telugu


ఎలా FIR నమోదు చేయాలి?
భూమి వివాదం ఉంటే ఏమి చేయాలి?


Hindi


एफआईआर कैसे दर्ज करें?
महिलाओं के अधिकार क्या हैं?


---

## Testing Queries

Example queries for testing:

- What are fundamental rights in India
- How to file consumer complaint
- Women protection laws in India
- Property registration process
- IPC Section 420 explanation

---

## Future Enhancements

- Add more legal document datasets
- Improve voice assistant capabilities
- Deploy the system on cloud
- Add user authentication and chat history
- Develop mobile-friendly interface

---

## Disclaimer

LAWBot provides general legal information only.

It should not be considered a substitute for professional legal advice.  
For specific legal matters, users should consult a qualified lawyer.

---

## Developer

Thushar Gurrala  
B.Tech – Computer Science (AI & ML)

GitHub: https://github.com/ThusharGurrala 

---

## License

This project is licensed under the MIT License.
