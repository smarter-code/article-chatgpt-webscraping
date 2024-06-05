import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the web page content
url = "https://quotes.toscrape.com"
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract the specific quote and author
quote_selector = "body > div.container > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span.text"
author_selector = "body > div.container > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span:nth-child(2) > small"

specific_quote = soup.select_one(quote_selector).get_text()
specific_author = soup.select_one(author_selector).get_text()

print(f"Specific Quote: {specific_quote}")
print(f"Specific Author: {specific_author}")

# Step 4: Extract all quotes and authors
quotes = soup.find_all('div', class_='quote')

all_quotes = []
for quote in quotes:
  text = quote.find('span', class_='text').get_text()
  author = quote.find('small', class_='author').get_text()
  all_quotes.append({"quote": text, "author": author})

# Step 5: Save the quotes to an Excel file
df = pd.DataFrame(all_quotes)
df.to_excel('quotes.xlsx', index=False)

print("Quotes have been saved to quotes.xlsx")soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract the specific quote and author
quote_selector = "body > div.container > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span.text"
author_selector = "body > div.container > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span:nth-child(2) > small"

specific_quote = soup.select_one(quote_selector).get_text()
specific_author = soup.select_one(author_selector).get_text()

print(f"Specific Quote: {specific_quote}")
print(f"Specific Author: {specific_author}")

# Step 4: Extract all quotes and authors
quotes = soup.find_all('div', class_='quote')

all_quotes = []
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    all_quotes.append({"quote": text, "author": author})

# Step 5: Save the quotes to an Excel file
df = pd.DataFrame(all_quotes)
df.to_excel('quotes.xlsx', index=False)

print("Quotes have been saved to quotes.xlsx")
