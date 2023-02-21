import yfinance as yf

# Download Tesla stock data
tesla_data = yf.download("TSLA", start="2021-01-01", end="2022-12-31")

# Reset the index
tesla_data = tesla_data.reset_index()

# Save the data to a CSV file
tesla_data.to_csv("tesla_stock_data.csv", index=False)

# Display the first five rows of the dataframe
print(tesla_data.head())