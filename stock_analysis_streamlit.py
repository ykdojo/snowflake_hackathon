import streamlit as st
import plotly.express as px
import pandas as pd
from stock_analysis import combine_data

# Define a list of available stock tickers
available_tickers = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]

# Create a multiselect dropdown menu for stock tickers
selected_tickers = st.multiselect(
    label="Select Stock Tickers",
    options=available_tickers,
    default=["AAPL"],  # Default selected value(s)
)

# Initialize an empty DataFrame to store the combined data
df_combined = pd.DataFrame()

# Perform analysis or visualization based on the selected stock tickers
for ticker in selected_tickers:
    # Filter the combined data for the selected stock ticker
    df_ticker = combine_data(ticker)
    # Add a new column to indicate the ticker symbol
    df_ticker["Ticker"] = ticker
    # Concatenate the data to the combined DataFrame
    df_combined = pd.concat([df_combined, df_ticker], ignore_index=True)

# Create a line plot using Plotly Express for stock price
fig = px.line(
    df_combined,
    x="DATE",
    y="Close",
    color="Ticker",
    labels={"Close": "Stock Price", "DATE": "Date"},
    title="Stock Price for Selected Stock Tickers",
)

# Create a line plot for TOTAL_VISITS
fig_total_visits = px.line(
    df_combined,
    x="DATE",
    y="TOTAL_VISITS",
    color="Ticker",
    labels={"TOTAL_VISITS": "Total Website Visits", "DATE": "Date"},
    title="Total Wbsite Visits for Selected Stock Tickers",
)

# Calculate relative change for Close (stock price) and set starting value to 100
for ticker in selected_tickers:
    df_combined.loc[df_combined["Ticker"] == ticker, "Relative_Close"] = (
        df_combined[df_combined["Ticker"] == ticker]["Close"]
        / df_combined[df_combined["Ticker"] == ticker]["Close"].iloc[0]
        * 100
    )
    df_combined.loc[df_combined["Ticker"] == ticker, "Relative_TOTAL_VISITS"] = (
        df_combined[df_combined["Ticker"] == ticker]["TOTAL_VISITS"]
        / df_combined[df_combined["Ticker"] == ticker]["TOTAL_VISITS"].iloc[0]
        * 100
    )

# Create a line plot for relative change in stock price
fig_relative_close = px.line(
    df_combined,
    x="DATE",
    y="Relative_Close",
    color="Ticker",
    labels={"Relative_Close": "Relative Stock Price", "DATE": "Date"},
    title="Relative Change in Stock Price (Starting Value = 100)",
)

# Create a line plot for relative change in total visits
fig_relative_total_visits = px.line(
    df_combined,
    x="DATE",
    y="Relative_TOTAL_VISITS",
    color="Ticker",
    labels={"Relative_TOTAL_VISITS": "Relative Total Visits", "DATE": "Date"},
    title="Relative Change in Total Website Visits (Starting Value = 100)",
)

stock_absolute, stock_relative = st.tabs(["Stock Price", "Relative Change"])
with stock_absolute:
    st.plotly_chart(fig)
with stock_relative:
    st.plotly_chart(fig_relative_close)

visits_absolute, visits_relative = st.tabs(["Total Website Visits", "Relative Change"])
with visits_relative:
    st.plotly_chart(fig_relative_total_visits)
with visits_absolute:
    st.plotly_chart(fig_total_visits)

# Create a line plot for S_MEAN (average sentiment score)
fig_s_mean = px.line(
    df_combined,
    x="DATE",
    y="S_MEAN",
    color="Ticker",
    labels={"S_MEAN": "Average Sentiment Score", "DATE": "Date"},
    title="Average Sentiment Score for Selected Stock Tickers",
)
st.plotly_chart(fig_s_mean)
