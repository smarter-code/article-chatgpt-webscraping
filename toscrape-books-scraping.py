import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = 'https://books.toscrape.com'

# Send a GET request to the website
response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Initialize lists to store the titles and prices
    book_titles = []
    book_prices = []

    # Extract the first book title and price using the provided selectors
    book_title_selector = "#default > div.container-fluid.page > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > h3 > a"
    book_price_selector = "#default > div.container-fluid.page > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > div.product_price > p.price_color"

    title_element = soup.select_one(book_title_selector)
    price_element = soup.select_one(book_price_selector)
    
    if title_element and price_element:
        book_titles.append(title_element.get('title'))
        book_prices.append(price_element.text.strip()[1:])

    # Extract all book titles and prices on the first page
    books = soup.select('section > div:nth-child(2) > ol > li')
    for book in books:
        title = book.select_one('h3 > a')
        price = book.select_one('div.product_price > p.price_color')
        if title and price:
            book_titles.append(title.get('title'))
            book_prices.append(price.text.strip()[1:])

    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Title': book_titles,
        'Price': book_prices
    })

    # Save the DataFrame to an Excel file
    df.to_excel('books_scraped.xlsx', index=False)

    print('Data has been successfully scraped and saved to books_scraped.xlsx')
else:
    print('Failed to retrieve the webpage')
