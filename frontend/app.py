import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="FinAI - Agentic Investment Advisor", layout="wide")
st.title("💸 FinAI — Agentic AI Investment Advisor")

company = st.text_input("Enter Stock Symbol (e.g., TCS.NS, RELIANCE.NS):", "TCS.NS")
risk = st.selectbox("Select Risk Appetite:", ["Low", "Medium", "High"])
budget = st.number_input("Investment Budget (₹):", min_value=1000.0, value=10000.0)

if st.button("Analyze Investment"):
    with st.spinner("FinAI is analyzing market data..."):
        response = requests.get(f"{API_URL}/analyze/{company}/{risk}?budget={budget}")
        if response.status_code == 200:
            result = response.json()

            st.subheader("📈 Sentiment Analysis")
            st.write(f"**Sentiment:** {result['sentiment']} ({result['score']})")

            st.subheader("📰 Latest Headlines")
            for h in result['headlines']:
                st.markdown(f"- {h}")

            st.subheader("🤖 FinAI's Advice")
            st.success(result['advice'])

            st.subheader("💼 Suggested Portfolio")
            portfolio_df = pd.DataFrame(result['portfolio'].items(), columns=["Asset", "Amount (₹)"])
            st.dataframe(portfolio_df)
            st.bar_chart(portfolio_df.set_index("Asset"))
        else:
            st.error("Backend API error. Please try again.")
