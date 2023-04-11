import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd

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

print('Creating a connection to Snowflake...')
# Create a connection to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Query to retrieve sentiment data
query_sentiment = f"""
SELECT *
FROM {DB_SENTIMENT}.{SCHEMA_SENTIMENT}.V_SUMMARY_BY_TOPIC_STOCK_15MIN
WHERE TICKER = '{TICKER}'
"""

# Query to retrieve website traffic data
query_traffic = f"""
SELECT *
FROM {DB_TRAFFIC}.{SCHEMA_TRAFFIC}.SP_500_ESTIMATED_TICKERS
WHERE TICKER = '{TICKER}'
"""

print('Executing sentiment data query...')
# Execute queries and fetch results
cur.execute(query_sentiment)
result_sentiment = cur.fetchall()
print('Executing website traffic data query...')
cur.execute(query_traffic)
result_traffic = cur.fetchall()

# Convert results to DataFrames
# Debugging: Print column names and data
print('Number of column names:', len([desc[0] for desc in cur.description]))
print('Column names:', [desc[0] for desc in cur.description])
print('Number of columns in data:', len(result_sentiment[0]))
print('Sentiment data (first 5 rows):', result_sentiment[:5])

# Create DataFrame
df_sentiment = pd.DataFrame(result_sentiment, columns=[desc[0] for desc in cur.description])
df_traffic = pd.DataFrame(result_traffic, columns=[desc[0] for desc in cur.description])

# Close the cursor and connection
cur.close()
conn.close()

# TODO: Retrieve stock price history data from an external API

# TODO: Standardize date formats across all data sources

# Print the DataFrames (for demonstration purposes)
print('Sentiment Data:')
print(df_sentiment.head())
print('Website Traffic Data:')
print(df_traffic.head())
