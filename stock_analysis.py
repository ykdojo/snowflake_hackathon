import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd
import yfinance as yf  # Import the yfinance library

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables
SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')

# Define the Snowflake databases and schemas
DB_SENTIMENT = 'SFACTOR_SOCIAL_SENTIMENT_DATA_FOR_US_EQUITIES'
SCHEMA_SENTIMENT = 'PUBLIC'
DB_TRAFFIC = 'SP_500_COMPANY_ONLINE_PERFORMANCE_TICKER_AND_DOMAIN_LEVEL_DATA'
SCHEMA_TRAFFIC = 'DATAFEEDS'

# Define the stock ticker to analyze
TICKER = 'AAPL'

# Create a reusable function for executing SQL queries and fetching results
def execute_query_and_fetch_results(conn, query):
    with conn.cursor() as cur:
        cur.execute(query)
        results = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
    return pd.DataFrame(results, columns=columns)

# Define queries
query_sentiment = f"""
SELECT *
FROM {DB_SENTIMENT}.{SCHEMA_SENTIMENT}.V_SUMMARY_BY_TOPIC_STOCK_15MIN
WHERE TICKER = '{TICKER}'
"""
query_traffic = f"""
SELECT *
FROM {DB_TRAFFIC}.{SCHEMA_TRAFFIC}.SP_500_ESTIMATED_TICKERS
WHERE TICKER = '{TICKER}'
"""

# Create a connection to Snowflake and execute queries
with snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE
) as conn:
    print('Executing sentiment data query...')
    df_sentiment = execute_query_and_fetch_results(conn, query_sentiment)
    print('Executing website traffic data query...')
    df_traffic = execute_query_and_fetch_results(conn, query_traffic)

# Standardize date formats across all data sources
df_sentiment['DATE'] = pd.to_datetime(df_sentiment['DATE'])
df_traffic['DATE'] = pd.to_datetime(df_traffic['DATE'])

# Print the date ranges and frequencies for each DataFrame
print('Sentiment Data Date Range:', df_sentiment['DATE'].min(), 'to', df_sentiment['DATE'].max())
print('Sentiment Data Frequency:', (df_sentiment['DATE'].diff().value_counts().idxmax()))

print('Website Traffic Data Date Range:', df_traffic['DATE'].min(), 'to', df_traffic['DATE'].max())
print('Website Traffic Data Frequency:', (df_traffic['DATE'].diff().value_counts().idxmax()))

# Retrieve stock price data from Yahoo Finance
print('Retrieving stock price data from Yahoo Finance...')
df_stock_price = yf.download(TICKER, period='max')

# Reset the index of the stock price DataFrame
df_stock_price.reset_index(inplace=True)

# Print the date ranges and frequencies for the stock price data
print('Stock Price Data Date Range:', df_stock_price['Date'].min(), 'to', df_stock_price['Date'].max())
print('Stock Price Data Frequency:', (df_stock_price['Date'].diff().value_counts().idxmax()))

# Import the yfinance library
import yfinance as yf

# Retrieve stock price data from Yahoo Finance
print('Retrieving stock price data from Yahoo Finance...')
df_stock_price = yf.download(TICKER, start=df_sentiment['DATE'].min(), end=df_sentiment['DATE'].max())

# Reset the index of the stock price DataFrame
df_stock_price.reset_index(inplace=True)

# Resample the sentiment data to daily frequency (aggregating only numeric columns)
numeric_cols = df_sentiment.select_dtypes(include=['number']).columns
df_sentiment_daily = df_sentiment[['DATE'] + list(numeric_cols)].copy()
df_sentiment_daily.set_index('DATE', inplace=True)
df_sentiment_daily = df_sentiment_daily.resample('D').mean()
df_sentiment_daily.reset_index(inplace=True)

# Merge the stock price data with the daily sentiment and website traffic data based on the date
df_combined = pd.merge(df_sentiment_daily, df_traffic, left_on='DATE', right_on='DATE', how='inner')
df_combined = pd.merge(df_combined, df_stock_price, left_on='DATE', right_on='Date', how='inner')

# Drop the duplicate 'Date' column
df_combined.drop(columns=['Date'], inplace=True)

# Check for missing values in the combined DataFrame
missing_values = df_combined.isnull().sum()
if missing_values.any():
    print('Missing values detected:')
    print(missing_values)
    # Handle missing values (e.g., interpolation, forward-filling, etc.)
    df_combined.fillna(method='ffill', inplace=True)
    df_combined.fillna(method='bfill', inplace=True)

# Print the combined DataFrame (for demonstration purposes)
print('Combined Data:')
print(df_combined.head())

# Print the date range and total number of rows in the combined DataFrame
print('Date Range:', df_combined['DATE'].min(), 'to', df_combined['DATE'].max())
print('Total Number of Rows (Days):', len(df_combined))
