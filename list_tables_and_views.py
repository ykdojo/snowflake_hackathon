import os
from dotenv import load_dotenv
import snowflake.connector

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables
SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')

# Define the Snowflake database and schema to check
DB_NAME = 'FINANCE_DATA_ATLAS'
SCHEMA_NAME = 'FINANCE'

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

# Query to list tables and views in the schema
cur.execute("SHOW TABLES")

# Fetch and print the results
tables_and_views = cur.fetchall()
for item in tables_and_views:
    print(item)

# Close the cursor and connection
cur.close()
conn.close()
