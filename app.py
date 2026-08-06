"""
Streamlit interface — frontend for the portfolio assistant.
"""

import streamlit as st
from rag import get_rag_chain

st.set_page_config(page_title="Portfolio Assistant", page_icon="👤")

st.title("👤 Portfolio Assistant")
st.caption("Hi! I'm [Your Name]'s assistant. Ask me about my experience and projects!")

# Initialize the RAG chain once (cached to avoid reloading on every question)
@st.cache_resource
def load_chain():
    return get_rag_chain()

chain = load_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("e.g. What are their main skills?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            result = chain.invoke({"query": prompt})
            response = result["result"]
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
