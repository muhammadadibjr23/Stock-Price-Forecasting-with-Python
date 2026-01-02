<div align="center">
<h1><b>Stock Price Forecasting with Python</b></h1>
<p align="justify">This repository contains the final project I developed during a training program on <b>Python Programming Fundamentals and Object-Oriented Programming (OOP)</b> organized by <b>PCI NU Netherlands</b>.</p>
<p align="justify">The training was supervised by:</p>
<p align="justify"><b>Dr. Rer. Nat. Trismono Candra Krisna</b></p>
<p align="justify">Mission Engineer at European Space Agency (ESA), Netherlands.</p>
</div>

<div align="center">
<a target="_blank" href="https://www.linkedin.com/in/muhammad-adib-b9b0962a6/"><img height="20" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a target="_blank" href=""><img height="20" src="https://img.shields.io/badge/License-MIT-green" alt="License"></a>
</div>

## 📄 Project Overview

The goal of this project is to build a Python program that can:

1. Retrieve historical stock price data from Yahoo Finance.
2. Perform interpolation by modeling the price trend using **Linear Regression**.
3. Perform extrapolation to generate a forecast of future stock prices for the next year.
4. Visualize historical prices, trend lines, and forecast results.

In simple terms:
The program analyzes the last 5 years of stock price movements and predicts the trend for the next 12 months.

## 💻 Tech Stack

This project was built using:
- `python`
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn` (Linear Regression)
- `yfinance` — primary data source from Yahoo Finance

## 🗂️ Project Structure
```
.
├── stock_price_forecasting.py
├── oop_stock_price_forecasting.py
├── requirements.txt
├── README.md
└── images/
    ├── pypl_stock_price_forecasting.png
    └── pypl_stock_price_forecasting_oop.png
```

## 🎯 Results

The project produces two visualizations:

### 1. General Implementation
Located in `images/stock_price_forecasting.png`

<img width="1400" height="700" alt="pypl_stock_price_forecasting" src="https://github.com/user-attachments/assets/e3dc64ba-3110-4f6a-9b0b-7003515afe00" />


### 2. Object-Oriented Implementation
Located in `images/stock_price_forecasting_oop.png`

<img width="1400" height="700" alt="pypl_stock_price_forecasting_oop" src="https://github.com/user-attachments/assets/861e1dd9-5d73-40aa-b0d5-5e0bafb50797" />

Both charts display:

- historical closing prices
- linear regression trend line
- one-year price forecast

## ⚙️ Installation & How to Run

### 1. Clone the repository

```
git clone <repository-link>
cd <repository-folder>
```

### 2. (Recommended) Create virtual environment

`python -m venv venv`

Activate:

- Windows

`venv\Scripts\activate`

- macOS / Linux:

`source venv/bin/activate`

### 3️. Install dependencies

`pip install -r requirements.txt`

### 4. Run the scripts
- Procedural version:

`python stock_price_forecasting.py`

- OOP version:

`python oop_stock_price_forecasting.py`

## ⚠️ Limitations & Disclaimer

This project uses simple Linear Regression as the forecasting model.

Therefore:
- it does not account for market volatility,
- it does not model non-linear behavior,
- it does not include external economic factors
- predictions are only illustrative
- This project is for educational purposes only and should not be used as financial trading advice.

## 📩 Contact

If you would like to discuss this project or provide feedback, feel free to reach out via:

GitHub Issues or email (adibjr23@gmail.com)



