# Stock Price Forecasting with Python

This repository contains the final project I developed during a training program on **Python Programming Fundamentals and Object-Oriented Programming (OOP)** organized by **PCI NU Netherlands**.

The training was supervised by:

**Dr. Rer. Nat. Trismono Candra Krisna**  
Mission Engineer — European Space Agency (ESA), Netherlands.

---

## 📌 Project Overview

The goal of this project is to build a Python program that can:

1. Retrieve historical stock price data from Yahoo Finance.
2. Perform interpolation by modeling the price trend using **Linear Regression**.
3. Perform extrapolation to generate a forecast of future stock prices for the next year.
4. Visualize historical prices, trend lines, and forecast results.

In simple terms:
The program analyzes the last 5 years of stock price movements and predicts the trend for the next 12 months.

---

## 🧰 Technologies & Libraries

This project was built using:
- `python`
- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn` (Linear Regression)
- `yfinance` — primary data source from Yahoo Finance

---

## 🗂️ Project Structure

```bash
.
├── stock_price_forecasting.py
├── oop_stock_price_forecasting.py
├── requirements.txt
├── README.md
└── images/
    ├── pypl_stock_price_forecasting.png
    └── pypl_stock_price_forecasting_oop.png

---

## 📊 Results

The project produces two visualizations:

### 1️⃣ Procedural implementation
Located in `stock_price_forecasting.py`

![PYPL Forecast](images/pypl_stock_price_forecast.png)

### 2️⃣ Object-Oriented implementation
Located in `oop_stock_price_forecasting.py`

![PYPL Forecast OOP](images/pypl_stock_price_forecast_oop.png)

Both charts display:

- historical closing prices
- linear regression trend line
- one-year price forecast

---

## ▶️ Installation & How to Run

### 1️⃣ Clone the repository

```bash
git clone <your-repository-link>
cd <repository-folder>

### 2️⃣ (Recommended) Create virtual environment

```bash
python -m venv venv

Activate:

- Windows
```bash
venv\Scripts\activate

- macOS / Linux:
```bash
source venv/bin/activate

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt

### 4️⃣ Run the scripts
- Procedural version:
```bash
python stock_price_forecasting.py

- OOP version:
python oop_stock_price_forecasting.py

---

## ⚠️ Limitations & Disclaimer

This project uses simple Linear Regression as the forecasting model.

Therefore:
- it does not account for market volatility,
- it does not model non-linear behavior,
- it does not include external economic factors
- predictions are only illustrative
- This project is for educational purposes only and should not be used as financial trading advice.

---

## 🙌 Acknowledgment

This project was completed as part of the Python training program organized by:

PCI NU Netherlands

under the supervision of:

Dr. Rer. Nat. Trismono Candra Krisna
Mission Engineer — European Space Agency (ESA), Netherlands.

---

## 📩 Contact

If you would like to discuss this project or provide feedback, feel free to reach out via:

GitHub Issues or email (adibjr23@gmail.com)



