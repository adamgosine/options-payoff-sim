# options-payoff-sim
#  Options Payoff Simulator

A Python project that simulates profit/loss for options trading strategies (starting with long calls) using **live market data** from Yahoo Finance.

This tool lets users:
- Pull real option chain data for any stock
- Simulate a range of expiration prices
- Visualize the profit/loss curve
- Identify breakeven, max loss, and risk/reward dynamics

##  Features

-  Long Call P&L Visualization
-  Live data from `yfinance`
-  Strategy modeling & breakeven analysis
-  Payoff curve export as PNG

##  Tech Stack

- Python
- yfinance
- pandas
- matplotlib

##  How to Run

```bash
pip install -r requirements.txt
python options_payoff.py

