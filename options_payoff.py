import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# === USER SETTINGS ===
ticker = "TSLA"           # Stock symbol
option_type = "call"      # 'call' or 'put'
strike_price = 250        # Your chosen strike
premium = 15              # Price paid for option
expiration_price_range = np.arange(150, 350, 5)  # Simulated stock prices

# === CALCULATE PAYOFF ===
def calculate_payoff(price_range, strike, premium, option_type):
    if option_type == "call":
        return np.maximum(price_range - strike, 0) - premium
    elif option_type == "put":
        return np.maximum(strike - price_range, 0) - premium
    else:
        raise ValueError("option_type must be 'call' or 'put'")

payoff = calculate_payoff(expiration_price_range, strike_price, premium, option_type)

# === PLOT ===
plt.figure(figsize=(10, 6))
plt.plot(expiration_price_range, payoff, label=f"Long {option_type.capitalize()}")
plt.axhline(0, color='black', linestyle='--')
plt.axvline(strike_price, color='red', linestyle='--', label='Strike Price')
plt.title(f"{ticker} {option_type.capitalize()} Option Payoff")
plt.xlabel("Stock Price at Expiration ($)")
plt.ylabel("Profit / Loss ($)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("payoff_plot.png")
plt.show()

