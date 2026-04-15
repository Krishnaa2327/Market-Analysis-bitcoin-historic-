# Trader Performance vs Market Sentiment

This project analyzes how market sentiment (Fear vs Greed) impacts trader behavior and performance using real trading data.

---

## Objective

To uncover patterns between market sentiment and:
- Trader profitability (PnL, win rate)
- Trading behavior (frequency, position size, leverage)

---

## Dataset

1. Bitcoin Fear & Greed Index  
2. Historical trader data (Hyperliquid)

---

## Key Features

- Data cleaning and preprocessing
- Sentiment-based analysis
- Behavioral analysis (trade size, frequency, long/short)
- Trader segmentation
- Interactive Streamlit dashboard

---

## Key Insights

- Highest profitability observed during **Extreme Greed**
- Fear conditions lead to **higher volatility and inconsistent trading**
- Larger trade sizes do not guarantee better returns
- Frequent traders underperform compared to selective traders

---

## Strategy Recommendations

- Reduce leverage during Fear phases
- Avoid overtrading in volatile conditions
- Focus on trade quality over quantity
- Adapt strategy dynamically based on sentiment

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Streamlit app

```bash
streamlit run app/app.py
```

---

## Project Structure

```text
project/
│
├── data/
│ ├── fear_greed_index.csv
│ └── historical_data.csv
│
├── app/
│ └── app.py
│
├── notebook/
│ └── analysis.ipynb
│
├── requirements.txt
└── README.md
```

---

## Deployment

You can deploy this app using:
- Streamlit Cloud
- Render
- Railway

---

## Author

Krishna Chaudhari  
Data Science Intern