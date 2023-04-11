import os
import pickle
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd
import yfinance as yf

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")

# Define the Snowflake databases and schemas
DB_SENTIMENT = "SFACTOR_SOCIAL_SENTIMENT_DATA_FOR_US_EQUITIES"
SCHEMA_SENTIMENT = "PUBLIC"
DB_TRAFFIC = "SP_500_COMPANY_ONLINE_PERFORMANCE_TICKER_AND_DOMAIN_LEVEL_DATA"
SCHEMA_TRAFFIC = "DATAFEEDS"

# Create a reusable function for executing SQL queries and fetching results
def execute_query_and_fetch_results(conn, query):
    with conn.cursor() as cur:
        cur.execute(query)
        results = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
    return pd.DataFrame(results, columns=columns)

# Define queries to retrieve stock tickers from each data source
query_sentiment_tickers = f"SELECT DISTINCT TICKER FROM {DB_SENTIMENT}.{SCHEMA_SENTIMENT}.V_SUMMARY_BY_TOPIC_STOCK_15MIN;"
query_traffic_tickers = f"SELECT DISTINCT TICKER FROM {DB_TRAFFIC}.{SCHEMA_TRAFFIC}.SP_500_ESTIMATED_TICKERS;"

# Create a connection to Snowflake and execute queries
with snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
) as conn:
    sentiment_tickers = set(execute_query_and_fetch_results(conn, query_sentiment_tickers)['TICKER'])
    traffic_tickers = set(execute_query_and_fetch_results(conn, query_traffic_tickers)['TICKER'])

# Retrieve S&P 500 tickers
import bs4 as bs
import requests

def get_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text.strip()
        tickers.append(ticker)
    return tickers

stock_price_tickers = set(get_sp500_tickers())

# Find the common tickers among all three data sources
common_tickers = sentiment_tickers.intersection(traffic_tickers, stock_price_tickers)

# Print the list of common stock tickers
print("List of common stock tickers among all three data sources:")
for ticker in common_tickers:
    print(ticker)
