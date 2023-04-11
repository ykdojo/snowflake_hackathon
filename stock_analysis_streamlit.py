import streamlit as st
import plotly.express as px
from stock_analysis import df_combined  # Import df_combined from stock_analysis.py

# Define a list of available stock tickers
available_tickers = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'TSLA']

# Create a multiselect dropdown menu for stock tickers
selected_tickers = st.multiselect(
    label='Select Stock Tickers',
    options=available_tickers,
    default=['AAPL']  # Default selected value(s)
)

# Perform analysis or visualization based on the selected stock tickers
for ticker in selected_tickers:
    # Filter the combined data for the selected stock ticker
    df_ticker = df_combined[df_combined['TICKER'] == ticker]
    
    # Create a line plot using Plotly Express
    fig = px.line(df_ticker, x='DATE', y=['TOTAL_VISITS', 'Close', 'S_MEAN'],
                  labels={'value': 'Values', 'variable': 'Metrics'},
                  title=f'Trends for {ticker}')
    
    # Display the plot in Streamlit
    st.plotly_chart(fig)
