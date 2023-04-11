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
SNOWFLAKE_DATABASE = 'SFACTOR_SOCIAL_SENTIMENT_DATA_FOR_US_EQUITIES'
SNOWFLAKE_SCHEMA = 'PUBLIC'

# Create a connection to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Execute a sample query (replace with your own query)
cur.execute("SELECT * FROM V_SUMMARY_BY_TOPIC_STOCK_15MIN LIMIT 10")

# Fetch the result of the query
result = cur.fetchall()

# Print the result
print("Schemas in the Snowflake database:")
# Print column labels
column_labels = [desc[0] for desc in cur.description]
print(column_labels)
# Print rows
for schema in result:
    print(schema)

# Close the cursor and connection
cur.close()
conn.close()
