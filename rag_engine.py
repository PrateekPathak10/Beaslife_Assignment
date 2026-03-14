from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faq_index",
    embeddings,
    allow_dangerous_deserialization=True
)

llm = Ollama(model="llama3")


def generate_response(query):

    docs = db.similarity_search(query)

    context = docs[0].page_content

    prompt = f"""
Use the following information to answer the customer query.

Context:
{context}

Customer Question:
{query}
"""

    response = llm.invoke(prompt)

    return response