def reorder_tickers_alphabetically(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Sort the tickers alphabetically
    sorted_lines = sorted(lines, key=lambda line: line.strip())

    # Write the sorted tickers back to the file
    with open(file_path, 'w') as file:
        file.writelines(sorted_lines)

# Define the path to the file containing the common stock tickers
common_tickers_file = 'projects/snowflake_hackathon/common_tickers_list.txt'

# Reorder the tickers in the file alphabetically
reorder_tickers_alphabetically(common_tickers_file)