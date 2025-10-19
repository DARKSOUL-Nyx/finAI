# agents/decision_agent.py
import os
from dotenv import load_dotenv
from typing import Dict, Any
import math

# LangChain / OpenAI imports
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

from backend.models import generate_portfolio


load_dotenv()


# Initialize model (temperature low for deterministic advice)
llm = ChatOpenAI(base_url="https://openrouter.ai/api/v1", temperature=0.2, max_tokens=700)

def _format_portfolio(portfolio: Dict[str, float]) -> str:
    lines = []
    total = sum(portfolio.values()) if portfolio else 0.0
    for k, v in portfolio.items():
        pct = (v / total * 100) if total > 0 else 0
        lines.append(f"- {k}: ₹{v:.2f} ({pct:.1f}%)")
    lines.append(f"Total: ₹{total:.2f}")
    return "\n".join(lines)

def agentic_response(
    user_message: str,
    ticker: str,
    portfolio: Dict[str, float],
    sentiment_label: str,
    sentiment_score: float,
    risk_level: str,
    latest_price: float,
    market_notes: str = "",
    chat_history: list = None,
    headlines: list = None
) -> Dict[str, Any]:
    """
    Generates an agentic response using a language model, incorporating chat history.
    """
    if chat_history is None:
        chat_history = []

    # Prepare the prompt for the language model
    portfolio_text = _format_portfolio(portfolio)
    prompt_system = SystemMessage(content=(
        "You are FinGenie, an expert financial advisor. "
        "When asked to analyze a portfolio and a single stock, you must: "
        "1) give a short summary, 2) list the main reasons behind your recommendation, "
        "3) give concrete recommendations (buy/sell/hold + size), "
        "4) provide a short, prioritized action plan the user can follow, "
        "5) output a confidence estimate (low/medium/high) and a numeric confidence (0-100). "
        "Prefer conservative language for low-risk users and more assertive language for high-risk users. "
        "Use bullet points for lists. Keep numeric values explicit (e.g., amounts or percentages)."
        "You should also respond to general chat messages and remember the history of the conversation."
    ))

    # Add the chat history to the prompt
    prompt_history = [SystemMessage(content="Here is the chat history:")]
    for message in chat_history:
        prompt_history.append(HumanMessage(content=f"User: {message['user']}"))
        prompt_history.append(SystemMessage(content=f"AI: {message['ai']}"))

    prompt_user = HumanMessage(content=(
        f"The user's message is: {user_message}\n\n"
        f"Analyze the ticker: {ticker}\n\n"
        f"Portfolio snapshot:\n{portfolio_text}\n\n"
        f"Latest price for {ticker}: ₹{latest_price:.2f}\n"
        f"Market sentiment: {sentiment_label} (score {sentiment_score:.3f})\n"
        f"User risk tolerance: {risk_level}\n"
        f"Market notes: {market_notes}\n\n"
        "Deliverables (strictly):\n"
        "1) Short summary (1-2 sentences).\n"
        "2) Key reasons supporting the recommendation (3 bullets).\n"
        "3) Recommendation: for the user give precise actions (e.g., 'Buy 10% of portfolio into RELIANCE.NS' or 'Sell 15% of BITCOIN').\n"
        "4) A step-by-step action plan (3 steps max) with estimated amounts.\n"
        "5) Confidence: one-word label and a numeric 0-100 confidence.\n\n"
        "Return the answer as plain text, with each of the five parts clearly labeled."
    ))

    # Call the LLM
    response = llm([prompt_system] + prompt_history + [prompt_user])
    text = response.content

    # Simple parsing: we will return the raw text plus minimal structure.
    # In a production system, you would instruct the model to reply in JSON and parse.
    return {
        "raw_text": text,
        "ticker": ticker,
        "portfolio": portfolio,
        "sentiment_label": sentiment_label,
        "sentiment_score": sentiment_score,
        "risk_level": risk_level,
        "headlines": headlines,
    }

