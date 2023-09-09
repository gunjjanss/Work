import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page with revenue data
url = 'https://stockanalysis.com/stocks/nke/revenue/'

# Fetch the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Locate the table with the specified class
table = soup.find('table', {'class': 'svelte-1jtwn20'})

# Extract table headings
headings = []
for th in table.find_all('th'):
    headings.append(th.text.strip())

# Extract table rows
rows = []
for tr in table.find_all('tr'):
    row = [td.text.strip() for td in tr.find_all('td')]
    if row:
        rows.append(row)

# Create a Pandas DataFrame
df = pd.DataFrame(rows, columns=headings)

# Print the DataFrame
print(df)


# Save DataFrame to Excel file
excel_filename = 'nike_annual_revenue_data.xlsx'
df.to_excel(csv_filename, index=False)

print(f"Data saved to {csv_filename}")