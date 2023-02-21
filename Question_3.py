import yfinance as yf

# Download GameStop stock data
gme_data = yf.download("GME", start="2021-01-01", end="2022-12-31")

# Reset the index
gme_data = gme_data.reset_index()

# Save the data to a CSV file
gme_data.to_csv("gme_stock_data.csv", index=False)

# Display the first five rows of the dataframe
print(gme_data.head())