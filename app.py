import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title="Beastlife AI Dashboard", layout="wide")

st.title("Beastlife AI Customer Intelligence Dashboard")

try:
    df = pd.read_csv("dataset.csv")
except:
    st.error("dataset.csv not found")
    st.stop()

if len(df) == 0:
    st.warning("No data available")
    st.stop()


st.subheader("Total Queries")

st.metric("Queries Received", len(df))


st.subheader("Issue Distribution")

category_counts = df["category"].value_counts()

fig = px.pie(
    values=category_counts.values,
    names=category_counts.index,
    title="Customer Issues Distribution"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Query Trend")

df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed")

trend = df.groupby(df["timestamp"].dt.date).size()

fig2 = px.line(
    x=trend.index,
    y=trend.values,
    labels={"x": "Date", "y": "Number of Queries"}
)

st.plotly_chart(fig2, use_container_width=True)


st.subheader("Recent Queries")

st.dataframe(df.tail(10), use_container_width=True)


st.divider()
st.header("AI Customer Support Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask about your order, refund, delivery, etc.")

if user_input:

    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        r = requests.post(
            "http://127.0.0.1:8000/query",
            json={"message": user_input}
        )

        data = r.json()

        category = data.get("category", "Unknown")
        response = data.get("response", "No response returned from API")

        ai_text = f"""
**Category:** {category}

{response}
"""

    except Exception as e:
        ai_text = f"⚠️ Error connecting to API: {e}"

    # display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_text)

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_text
    })