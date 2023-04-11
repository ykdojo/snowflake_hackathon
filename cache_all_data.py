import pandas as pd
from stock_analysis import combine_data

# Load the updated CSV file with ticker-company mappings
ticker_df = pd.read_csv('updated_tickers_list.csv')

# Loop through all available tickers and cache data for each ticker
for ticker in ticker_df['Ticker']:
    print('\n' * 2 + f'Processing data for {ticker}...')
    # Call the combine_data function from stock_analysis.py to get and cache data for the current ticker
    df_combined = combine_data(ticker)
    print(f'Data for {ticker} has been processed and cached.')

print('All data has been processed and cached.')
