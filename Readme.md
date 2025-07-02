# Grandpa Assistant - Django + LangChain RAG AI App

This project is dedicated to building a Retrieval-Augmented Generation (RAG) AI assistant powered by LangChain and Django. It honors the memory of a beloved grandparent who taught and inspired coding through challenges and mentoring. The app allows users to upload notes and ask questions, returning intelligent answers using OpenAI and a vector-based search over embedded document chunks.

## 🧠 Core Concept
- **LangChain + FAISS** is used to implement Retrieval-Augmented Generation (RAG)
- **Django** serves as the backend API & admin interface
- **React (now added)** powers a chat-based frontend UI
- **OpenAI GPT-3.5/4** answers questions based on uploaded knowledge

---

## 🗂 Project Structure

```
grandpa_assistant/
├── backend/
│   ├── core/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── rag_utils.py
│   ├── grandpa_assistant/
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   └── ChatBox.jsx
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── api.js
│   ├── package.json
│   └── README.md
├── .env
└── README.md
```

---

## 🔧 Installation Guide

### 1. Backend (Python/Django)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env file
echo "OPENAI_API_KEY=your-key" > .env

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 2. Frontend (React)
```bash
cd ../frontend
npm install
npm run dev
```
Visit: [http://localhost:5173](http://localhost:5173)

---

#1: The backend Setup allow file upload and RAG over curated grandpa's notes.

Deliverables:

> POST /upload-note endpoint

> POST /ask-question endpoint

> http://127.0.0.1:8000/chat/

