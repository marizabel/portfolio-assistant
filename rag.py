"""
RAG core module — loads documents, creates embeddings,
and builds the question-answering chain.
"""

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import os

load_dotenv()

CHROMA_DB_PATH = "./chroma_db"
DATA_PATH = "./data"


def load_documents():
    """Loads all .md files from the data/ folder"""
    loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    return loader.load()


def create_vectorstore(documents):
    """Splits documents into chunks and creates the vector store"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_PATH
    )
    return vectorstore


def get_rag_chain():
    """Builds the full RAG chain"""
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    prompt = ChatPromptTemplate.from_template("""
    Answer the question based only on the following context:
    {context}

    Question: {question}
    """)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": vectorstore.as_retriever(search_kwargs={"k": 3}) | format_docs,
         "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain


def setup():
    """Run once to index documents into ChromaDB"""
    print("Loading documents...")
    docs = load_documents()
    print(f"{len(docs)} document(s) found.")
    create_vectorstore(docs)
    print("Vector store created successfully!")


if __name__ == "__main__":
    setup()
