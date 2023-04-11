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

# Print the DataFrames (for demonstration purposes)
print('Sentiment Data:')
print(df_sentiment.head())
print('Website Traffic Data:')
print(df_traffic.head())
