import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the GameStop revenue data
url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'

# Send a GET request to the website and get the HTML content
html_content = requests.get(url).text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "lxml")

# Find the revenue table in the HTML and extract the data
table = soup.find('table', id='style-1')
rows = table.tbody.find_all('tr')
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Convert the data to a pandas dataframe
headers = data.pop(0)
gme_revenue = pd.DataFrame(data, columns=headers)

# Display the last five rows of the dataframe
print(gme_revenue.tail())