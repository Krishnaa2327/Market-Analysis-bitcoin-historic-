import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Trader Sentiment Analysis", layout="wide")

st.title("Trader Performance vs Market Sentiment")

# Load data
@st.cache_data
def load_data():
    fear_greed = pd.read_csv("data/fear_greed_index.csv")
    trades = pd.read_csv("data/historical_data.csv")

    fear_greed['Date'] = pd.to_datetime(fear_greed['Date']).dt.date
    trades['time'] = pd.to_datetime(trades['time'])
    trades['Date'] = trades['time'].dt.date

    merged = pd.merge(trades, fear_greed, on='Date', how='inner')
    merged['win'] = (merged['closedPnL'] > 0).astype(int)

    return merged

df = load_data()

# Sidebar
st.sidebar.header("Filters")
sentiment = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['Classification'].unique(),
    default=df['Classification'].unique()
)

filtered_df = df[df['Classification'].isin(sentiment)]

# KPI Section
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Avg PnL", f"{filtered_df['closedPnL'].mean():.2f}")
col2.metric("Win Rate", f"{filtered_df['win'].mean():.2f}")
col3.metric("Avg Trade Size", f"{filtered_df['size'].mean():.2f}")

# PnL by Sentiment
st.subheader("Average PnL by Sentiment")
pnl = filtered_df.groupby('Classification')['closedPnL'].mean()
st.bar_chart(pnl)

# Win Rate
st.subheader("Win Rate by Sentiment")
win = filtered_df.groupby('Classification')['win'].mean()
st.bar_chart(win)

# Trade Frequency
st.subheader("Trade Frequency")
freq = filtered_df.groupby('Classification').size()
st.bar_chart(freq)

# Boxplot - PnL Distribution
st.subheader("PnL Distribution")
fig1, ax1 = plt.subplots()
sns.boxplot(x='Classification', y='closedPnL', data=filtered_df, ax=ax1)
st.pyplot(fig1)

# Trade Size Distribution
st.subheader("Trade Size Distribution")
fig2, ax2 = plt.subplots()
sns.boxplot(x='Classification', y='size', data=filtered_df, ax=ax2)
st.pyplot(fig2)

# Long vs Short
st.subheader("Long vs Short Behavior")
ls = filtered_df.groupby(['Classification', 'side']).size().unstack().fillna(0)
st.bar_chart(ls)

# Insights Section
st.subheader("Key Insights")

st.markdown("""
- Traders perform best during **Extreme Greed**, with highest PnL and win rate  
- Fear phases show **higher volatility and inconsistent trade sizes**  
- Large trade sizes do not guarantee profitability  
- Overtrading reduces performance; fewer trades often yield better results  
""")

# Footer
st.markdown("---")
st.caption("Built for Data Science Intern Assignment – Trader Behavior Analysis")