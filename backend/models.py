import json
import os
import pandas as pd
import numpy as np


def calculate_portfolio_distribution(budget: float, risk_level: str):
    if risk_level == "High":
        return {
            "Stocks": budget * 0.7,
            "Mutual Funds": budget * 0.2,
            "Gold/Bonds": budget * 0.1
        }
    elif risk_level == "Medium":
        return {
            "Stocks": budget * 0.5,
            "Mutual Funds": budget * 0.3,
            "Gold/Bonds": budget * 0.2
        }
    else:
        return {
            "Stocks": budget * 0.3,
            "Mutual Funds": budget * 0.4,
            "Gold/Bonds": budget * 0.3
        }


# Simple risk-based portfolio allocation
def generate_portfolio(risk_level):
    if risk_level == "Low":
        portfolio = {
            "Bonds": 60,
            "Large Cap Stocks": 25,
            "Gold ETF": 10,
            "Cash": 5
        }
    elif risk_level == "Medium":
        portfolio = {
            "Large Cap Stocks": 40,
            "Mid Cap Stocks": 30,
            "Gold ETF": 20,
            "Cash": 10
        }
    else:
        portfolio = {
            "Mid Cap Stocks": 40,
            "Small Cap Stocks": 30,
            "Crypto/High-Risk": 20,
            "Cash": 10
        }
    return portfolio

def portfolio_dataframe(portfolio_dict):
    df = pd.DataFrame(list(portfolio_dict.items()), columns=["Asset", "Allocation (%)"])
    return df


def save_user_portfolio(username, risk_level, portfolio):
    os.makedirs("data", exist_ok=True)
    path = "data/user_portfolios.json"
    data = {}
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
    data[username] = {"risk": risk_level, "portfolio": portfolio}
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_user_portfolio(username):
    path = "data/user_portfolios.json"
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        data = json.load(f)
    return data.get(username, None)
