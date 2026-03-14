from fastapi import FastAPI
import pandas as pd
from datetime import datetime

from classifier import classify_query
from rag_engine import generate_response

app = FastAPI()

DATA_FILE = "dataset.csv"

try:
    df = pd.read_csv(DATA_FILE)
except:
    df = pd.DataFrame(columns=["message","category","response","timestamp"])


@app.post("/query")
def process_query(data: dict):

    message = data["message"]

    category = classify_query(message)

    response = generate_response(message)

    new_row = {
        "message": message,
        "category": category,
        "response": response,
        "timestamp": datetime.now()
    }

    global df
    df = pd.concat([df, pd.DataFrame([new_row])])

    df.to_csv(DATA_FILE, index=False)

    return {
        "category": category,
        "response": response
    }