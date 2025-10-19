import sys
import os
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.data_agent import fetch_stock_data as get_stock_data
from agents.sentiment_agent import analyze_sentiment
from backend.models import generate_portfolio, portfolio_dataframe

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="FinAI - Agentic Investment Advisor", layout="wide")
st.title("💸 FinAI — Agentic AI Investment Advisor")
st.caption("Empowering investors with AI-driven reasoning and personalized strategies")

# --- Sidebar ---
st.sidebar.header("Investor Preferences")
company = st.sidebar.text_input("Stock Symbol (e.g. TCS.NS)", "TCS.NS")
risk_level = st.sidebar.selectbox("Risk Level", ["Low", "Medium", "High"])
period = st.sidebar.selectbox("Data Period", ["1mo", "3mo", "6mo", "1y"])
budget = st.sidebar.number_input("Investment Budget (₹):", min_value=1000.0, value=10000.0)


# --- Stock Data Visualization ---
col1, col2 = st.columns(2)
with col1:
    st.subheader(f"📊 Stock Data: {company}")
    stock_data = get_stock_data(company, period)
    close_col = f"Close{company}"
    if isinstance(stock_data, pd.DataFrame) and not stock_data.empty and 'Date' in stock_data.columns and close_col in stock_data.columns:
        fig = px.line(stock_data, x="Date", y=close_col, title=f"{company} Price Trend")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error(f"Could not fetch stock data or find the close price column for {company}.")

# --- Sentiment ---
with col2:
    st.subheader("🧠 Market Sentiment")
    headlines = [{"headline": f"{company} shows steady Q2 performance"}, {"headline": f"Analysts bullish on {company}"}]
    sentiment_label, score = analyze_sentiment(headlines)
    st.metric("Sentiment", sentiment_label, f"{score:.2f}")

# # --- Portfolio Section ---
# st.markdown("### 💼 Personalized Portfolio Suggestion")
# portfolio = generate_portfolio(risk_level)
# pf_df = portfolio_dataframe(portfolio)
# fig_pf = px.pie(pf_df, names='Asset', values='Allocation (%)', title='Recommended Portfolio Distribution')
# st.plotly_chart(fig_pf, use_container_width=True)
# st.dataframe(pf_df, use_container_width=True)

# --- Chat Agent ---
st.markdown("### 💬 Chat with FinAI Advisor")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Ask FinAI anything (e.g. 'Should I buy TCS?', 'Show my portfolio')"):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("FinAI is thinking..."):
            response = requests.get(f"{API_URL}/analyze/{company}/{risk_level}?budget={budget}&user_message={user_query}", json={"chat_history": st.session_state.messages})
            if response.status_code == 200:
                result = response.json()
                st.markdown(result["raw_text"])
                st.session_state.messages.append({"role": "assistant", "content": result["raw_text"]})
            else:
                st.error("Backend API error. Please try again.")