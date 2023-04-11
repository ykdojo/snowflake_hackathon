import streamlit as st
import matplotlib.pyplot as plt
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
    # (Assuming 'TICKER' is the column representing the stock ticker in df_combined)
    # Perform analysis or visualization based on the selected stock tickers
    df_ticker = df_combined[df_combined['TICKER'] == ticker]
    
    # Line plot showing trends over time
    plt.figure(figsize=(10, 6))
    plt.plot(df_ticker['DATE'], df_ticker['TOTAL_VISITS'], label='Total Visits')
    plt.plot(df_ticker['DATE'], df_ticker['Close'], label='Stock Price (Close)')
    plt.plot(df_ticker['DATE'], df_ticker['S_MEAN'], label='Sentiment Mean (S_MEAN)')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(f'Trends of Total Visits, Stock Price, and Sentiment Mean ({ticker})')
    plt.legend()
    st.pyplot(plt)
    plt.clf()
    
    # Scatter plot showing relationship between Total Visits and Close with Sentiment Mean as color scale
    plt.figure(figsize=(10, 6))
    plt.scatter(df_ticker['TOTAL_VISITS'], df_ticker['Close'], c=df_ticker['S_MEAN'], cmap='coolwarm', label='Sentiment Mean')
    plt.colorbar(label='Sentiment Mean (S_MEAN)')
    plt.xlabel('Total Visits')
    plt.ylabel('Stock Price (Close)')
    plt.title(f'Total Visits vs. Stock Price with Sentiment Mean ({ticker})')
    st.pyplot(plt)
    plt.clf()
    
    # Scatter plot showing relationship between Sentiment Mean and Close with Total Visits as size scale
    plt.figure(figsize=(10, 6))
    plt.scatter(df_ticker['S_MEAN'], df_ticker['Close'], s=df_ticker['TOTAL_VISITS']/1000, alpha=0.5, label='Total Visits')
    plt.xlabel('Sentiment Mean (S_MEAN)')
    plt.ylabel('Stock Price (Close)')
    plt.title(f'Sentiment Mean vs. Stock Price with Total Visits ({ticker})')
    plt.legend()
    st.pyplot(plt)
    plt.clf()
    
    # # Plot the stock price over time
    # plt.figure(figsize=(10, 6))
    # plt.plot(df_ticker['DATE'], df_ticker['Close'], label='Stock Price')
    # plt.xlabel('Date')
    # plt.ylabel('Price')
    # plt.title(f'Stock Price Over Time ({ticker})')
    # plt.legend()
    # plt.show()

    # # Create a scatter plot to visualize the relationship between sentiment and stock price
    # # (Assuming 'SENTIMENT_VARIABLE' is the column representing sentiment data)
    # plt.figure(figsize=(10, 6))
    # plt.scatter(df_ticker['SENTIMENT_VARIABLE'], df_ticker['Close'], label='Sentiment vs. Price')
    # plt.xlabel('Sentiment')
    # plt.ylabel('Price')
    # plt.title(f'Sentiment vs. Stock Price ({ticker})')
    # plt.legend()
    # plt.show()
