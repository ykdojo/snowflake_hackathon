import streamlit as st

# Title
st.title('Stock Analysis Dashboard')

# Description
st.markdown("""
With this interactive tool, you can select stock tickers and explore trends in daily closing prices, website traffic, and sentiment scores. The dashboard provides visualizations of both absolute values and relative changes, giving you valuable insights into the performance of the selected stocks.
""")

# Separator
st.markdown('---')
import plotly.express as px
import pandas as pd
from stock_analysis import combine_data

# Define a list of available stock tickers
available_tickers = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]

# Create a multiselect dropdown menu for stock tickers
selected_tickers = st.multiselect(
    label="Select Stock Tickers",
    options=available_tickers,
    default=["AAPL", "GOOG", "MSFT"],
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
    title="Daily Closing Price for Selected Stock Tickers",
)

# Create a line plot for TOTAL_VISITS
fig_total_visits = px.line(
    df_combined,
    x="DATE",
    y="TOTAL_VISITS",
    color="Ticker",
    labels={"TOTAL_VISITS": "Total Website Visits", "DATE": "Date"},
    title="Total Website Visits for Selected Stock Tickers",
)

# Create a line plot for S_MEAN (average sentiment score)
fig_s_mean = px.line(
    df_combined,
    x="DATE",
    y="S_MEAN",
    color="Ticker",
    labels={"S_MEAN": "Average Sentiment Score", "DATE": "Date"},
    title="Average Sentiment Score for Selected Stock Tickers",
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
    df_combined.loc[df_combined["Ticker"] == ticker, "Relative_S_MEAN"] = (
        df_combined[df_combined["Ticker"] == ticker]["S_MEAN"]
        / df_combined[df_combined["Ticker"] == ticker]["S_MEAN"].iloc[0]
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

# Create a line plot for relative change in S_MEAN (average sentiment score)
fig_relative_s_mean = px.line(
    df_combined,
    x="DATE",
    y="Relative_S_MEAN",
    color="Ticker",
    labels={"Relative_S_MEAN": "Relative Sentiment Score", "DATE": "Date"},
    title="Relative Change in Sentiment Score (Starting Value = 100)",
)

stock_absolute, stock_relative = st.tabs(["Stock Price", "Relative Change"])
with stock_absolute:
    st.plotly_chart(fig)
with stock_relative:
    st.plotly_chart(fig_relative_close)

visits_relative, visits_absolute = st.tabs(["Relative Change", "Total Website Visits"])
with visits_relative:
    st.plotly_chart(fig_relative_total_visits)
with visits_absolute:
    st.plotly_chart(fig_total_visits)

sentiment_absolute, sentiment_relative = st.tabs(["Sentiment Score", "Relative Change"])
with sentiment_relative:
    st.plotly_chart(fig_relative_s_mean)
with sentiment_absolute:
    st.plotly_chart(fig_s_mean)


# Separator
st.markdown('---')

# Header for Combined Analysis
st.header('Combined Analysis')

# Description for Combined Analysis
st.markdown('Below are combined charts that show relative changes in stock price, website visits, and sentiment scores for each selected ticker. The charts provide a comprehensive view of how these three metrics have evolved over time, allowing you to identify correlations and trends that may impact the performance of the selected stocks.')

# Create a line plot for each selected ticker that combines relative change in stock price, total visits, and sentiment score
for ticker in selected_tickers:
    df_ticker = df_combined[df_combined["Ticker"] == ticker]
    # Reshape the data into a long format
    df_ticker_melted = pd.melt(
        df_ticker,
        id_vars=["DATE"],
        value_vars=["Relative_Close", "Relative_TOTAL_VISITS", "Relative_S_MEAN"],
        var_name="Metric",
        value_name="Relative Change",
    )
    # Map column names to more descriptive labels
    metric_labels = {
        "Relative_Close": "Relative Stock Price Change",
        "Relative_TOTAL_VISITS": "Relative Website Visit Change",
        "Relative_S_MEAN": "Relative Average Sentiment Score Change",
    }
    df_ticker_melted["Metric"] = df_ticker_melted["Metric"].map(metric_labels)

    # Create the line plot
    fig_combined = px.line(
        df_ticker_melted,
        x="DATE",
        y="Relative Change",
        color="Metric",
        labels={
            "DATE": "Date",
            "Relative Change": "Relative Change",
            "Metric": "Metric",
        },
        title=f"Combined Analysis for {ticker} (Starting Value = 100)",
    )
    st.plotly_chart(fig_combined)
