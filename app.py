import streamlit as st
import snowflake.connector

# Define the Streamlit app
def main():
    st.title("Snowflake and Streamlit Demo")
    st.write("Welcome to the Snowflake and Streamlit demo app!")

    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )

    # Execute a simple query
    query = "SELECT * FROM <YOUR_TABLE> LIMIT 10;"
    results = conn.cursor().execute(query).fetchall()

    # Display the results in the Streamlit app
    st.write(results)

    # Close the Snowflake connection
    conn.close()

# Run the Streamlit app
if __name__ == "__main__":
    main()