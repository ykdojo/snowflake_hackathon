import yfinance as yf

# Read the tickers from the existing text file
with open('common_tickers_list.txt', 'r') as f:
    tickers_list = f.read().splitlines()

# Create a dictionary to store ticker-company mappings
ticker_to_company = {}

# Iterate through the tickers and retrieve company names
for ticker_symbol in tickers_list:
    try:
        ticker = yf.Ticker(ticker_symbol)
        company_name = ticker.info['longName']
        ticker_to_company[ticker_symbol] = company_name
        print(f'Successfully retrieved data for {ticker_symbol}: {company_name}')
    except Exception as e:
        print(f'Error retrieving data for {ticker_symbol}: {e}')

# Write the updated ticker-company mappings to a new CSV file
import csv
with open('projects/snowflake_hackathon/updated_tickers_list.csv', 'w', newline='') as csvfile:
    fieldnames = ['Ticker', 'Company']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ticker, company in ticker_to_company.items():
        writer.writerow({'Ticker': ticker, 'Company': company})

print('Ticker-company mappings have been updated and saved to updated_tickers_list.txt.')