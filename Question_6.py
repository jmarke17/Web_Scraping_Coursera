import yfinance as yf
import matplotlib.pyplot as plt

# Define the make_graph function
def make_graph(x, y, title='', x_label='', y_label=''):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Download GameStop stock data
gme_data = yf.download("GME", start="2021-01-01", end="2022-12-31")

# Call the make_graph function to plot the data
make_graph(gme_data.index, gme_data['Close'], title='GameStop Stock Data 2020', x_label='Date', y_label='Closing Price')