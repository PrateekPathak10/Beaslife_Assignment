from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

categories = """
Order Status
Delivery Delay
Refund Request
Product Issue
Subscription Issue
Payment Problem
General Query
"""

def classify_query(message):

    prompt = f"""
Classify this customer message.

Categories:
{categories}

Message:
{message}

Return only category.
"""

    response = llm.invoke(prompt)

    return response.strip()