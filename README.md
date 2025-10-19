# 💸 FinAI — The Agentic AI Investment Advisor

Empowering investors with AI-driven reasoning and personalized financial strategies.

---

FinAI is a sophisticated financial advisor application that leverages a **multi-agent system** to provide insightful, data-driven investment advice.
It combines real-time market data, news sentiment analysis, and personalized user preferences to deliver **actionable recommendations** through an intuitive chat interface.

---

## 🚀 Key Features

### 📈 Real-Time Stock Analysis

Fetches and displays up-to-date stock data for any given ticker.

### 🧠 Market Sentiment Analysis

Scrapes financial news and analyzes sentiment using the **FinBERT** model.

### 🤖 Multi-Agent Architecture

A team of specialized AI agents collaborate to gather and process information:

* **Data Agent:** Fetches historical stock prices.
* **News Agent:** Gathers the latest financial news.
* **Sentiment Agent:** Analyzes the sentiment of news headlines.
* **Decision Agent:** Synthesizes all data to provide a final, reasoned recommendation.

### 💬 Interactive Chat Advisor

Chat with **FinGenie** to get personalized advice based on your risk tolerance and budget.

### 💼 Personalized Portfolio Suggestions

Generates a **custom portfolio distribution** based on your risk profile (Low, Medium, or High).

---

## 🧮 Tech Stack

**Frontend:**

* Streamlit

**Backend:**

* FastAPI

**AI & Machine Learning:**

* LangChain for LLM orchestration
* Transformers (FinBERT) for sentiment analysis
* OpenRouter for access to various LLMs (e.g., Google Gemini, Llama)

**Data & Analysis:**

* Pandas for data manipulation
* yfinance for stock data
* Plotly for interactive charts

---
[![Watch the video](https://drive.google.com/file/d/1hY-CKiyg9_VgxxpVUsTtdMkuDjHP5pPV/view?usp=sharing)](https://www.youtube.com/watch?v=uPH0AtPdygc)


---

## 🏁 Getting Started

Follow these steps to get the **FinAI** application running on your local machine.

### 1. Prerequisites

* Python 3.9+
* An **OpenRouter API Key**

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/finai.git
cd finai
```

### 3. Install Dependencies

Install all the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a file named `.env` in the root directory of the project and add your OpenRouter API key:

```bash
OPENROUTER_API_KEY="your_openrouter_api_key_here"
```

### 5. Run the Application

You’ll need two separate terminal windows to run both the backend and the frontend.

**Backend:**

```bash
uvicorn backend.api:app --reload
```

**Frontend:**

```bash
streamlit run frontend/app.py
```

Then open your browser and navigate to **[http://localhost:8501](http://localhost:8501)** to start using FinAI!

---

## ⚙️ How It Works

The application is built with a **decoupled frontend and backend**, communicating via REST API.
The core logic is handled by a team of AI agents:

1. **User Input:** The user provides a stock ticker, risk level, and budget through the Streamlit interface.
2. **Data Collection:** The Data Agent fetches historical stock data, while the News Agent scrapes recent headlines.
3. **Sentiment Analysis:** The Sentiment Agent uses FinBERT to determine if market sentiment is positive, negative, or neutral.
4. **Agentic Response:** All this data is passed to the Decision Agent, which uses an LLM (like Google Gemini Pro) to produce a reasoned investment recommendation.
5. **Display:** The final advice, charts, and sentiment scores are presented in the chat interface.

---

## 🤝 Contributing

We welcome contributions from the community!
To contribute:

1. **Fork** the repository.
2. **Create a new branch** for your feature or bug fix:

   ```bash
   git checkout -b feature/my-new-feature
   ```
3. **Make your changes** and commit them with a clear message.
4. **Push** to your branch and submit a **Pull Request**.

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

### ⭐ Support the Project

If you find **FinAI** useful, consider giving it a ⭐ on GitHub!
