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

# Define the Snowflake database, schema, and table
DB_NAME = 'FINANCE_DATA_ATLAS'
SCHEMA_NAME = 'FINANCE'
TABLE_NAME = 'DATASETS'

# Create a connection to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE
)

# Create a cursor object
cur = conn.cursor()

# Switch to the specified database and schema
cur.execute(f"USE DATABASE {DB_NAME}")
cur.execute(f"USE SCHEMA {SCHEMA_NAME}")

# Query to retrieve data from the DATASETS table
query = f"SELECT * FROM {TABLE_NAME}"

# Execute the query and fetch the results
cur.execute(query)
results = cur.fetchall()

# Convert the results to a Pandas DataFrame
columns = [desc[0] for desc in cur.description]
df = pd.DataFrame(results, columns=columns)

# Print the DataFrame
print(df)

# Close the cursor and connection
cur.close()
conn.close()

