from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open Yelp
    driver.get('https://www.yelp.com/')

    # Clear the location search box
    location_box = driver.find_element(By.CSS_SELECTOR, '#search_location')
    location_box.clear()

    # Enter "Stockholm" in the location search box
    location_box.send_keys('Stockholm')

    # Click the search button
    search_button = driver.find_element(By.CSS_SELECTOR, '#header_find_form > div.y-css-1iy1dwt > button')
    search_button.click()

    # Wait for search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#main-content'))
    )

    # Click on "Open Now" filter
    open_now_button = driver.find_element(By.CSS_SELECTOR, '#main-content > div.stickyFilterOnSmallScreen__09f24__UWWJ3.hideFilterOnLargeScreen__09f24__ilqIP.y-css-9ze9ku > div > div > div > div > div > span > button:nth-child(3) > span')
    open_now_button.click()

    # Wait for the filter results to load
    time.sleep(5)

    # Extract business names and reviews
    business_names = []
    business_reviews = []

    businesses = driver.find_elements(By.CSS_SELECTOR, '#main-content > ul > li')

    for business in businesses:
        try:
            name = business.find_element(By.CSS_SELECTOR, 'div.container__09f24__FeTO6.hoverable__09f24___UXLO.y-css-way87j > div > div.y-css-cxcdjj > div:nth-child(1) > div.y-css-1iy1dwt > div:nth-child(1) > div > div > h3 > a').text
            review = business.find_element(By.CSS_SELECTOR, 'div.container__09f24__FeTO6.hoverable__09f24___UXLO.y-css-way87j > div > div.y-css-cxcdjj > div:nth-child(1) > div.y-css-1iy1dwt > div:nth-child(2) > div > div > div > div.y-css-ohs7lg > span.y-css-jf9frv').text
            business_names.append(name)
            business_reviews.append(review)
        except Exception as e:
            print(f"Error extracting data for a business: {e}")

    # Create a DataFrame and save to Excel
    df = pd.DataFrame({'Business Name': business_names, 'Reviews': business_reviews})
    df.to_excel('stockholm_businesses.xlsx', index=False)
    print("Data saved to stockholm_businesses.xlsx")

finally:
    # Close the WebDriver
    driver.quit()
