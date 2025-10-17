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
