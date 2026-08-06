# 🤖 Portfolio Assistant

An AI assistant that answers questions about my professional experience using RAG (Retrieval-Augmented Generation).

## How it works

1. Documents about my career live in the `data/` folder
2. The system splits them into chunks and creates embeddings with `sentence-transformers`
3. Vectors are stored in ChromaDB
4. When someone asks a question, the system retrieves relevant chunks and sends them to Gemini to generate the answer

## Stack

- **LangChain** — RAG orchestration
- **Gemini Flash** — LLM (Google AI)
- **sentence-transformers** — local embeddings
- **ChromaDB** — vector database
- **Streamlit** — web interface

## Running locally

```bash
# 1. Create virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt

# 2. Set up environment variables
copy .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# 3. Index the documents (run once)
python rag.py

# 4. Start the app
streamlit run app.py
```
