import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Connection_to_wolt import *
from SaveInDB import *

def get_restaurant_links(url, search_text):

    cursor, conn = init_database()

    # Set up the Chrome driver
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()  # Set the browser to full screen

    try:
        # Open the Wolt page
        driver.get(url)

        # Wait for the button to be clickable, then click it
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ac320z2")))
        button.click()


        # Wait for the input field, enter search text, and press Enter
        search_input = wait.until(EC.presence_of_element_located((By.ID, "address-query-input")))
        time.sleep(3)
        search_input.send_keys(search_text)
        time.sleep(3)
        search_input.send_keys(Keys.RETURN)  # Press Enter

        time.sleep(3)
        search_input.send_keys(Keys.RETURN)  # Press Enter


        # Wait for the page to load new results (adjust wait time if needed)
        time.sleep(2)  # Add a delay to wait for the page to load

        # Scroll down to load more restaurants
        scroll_pause_time = 2  # Time to wait after each scroll, adjust as needed
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for the new content to load
            time.sleep(scroll_pause_time)

            # Check if we reached the end of the page
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # After scrolling, find all restaurant links
        restaurants = driver.find_elements(By.CLASS_NAME, "dzrkw9x")  # Adjust this class name if needed

        cities = returnCitiesNames(cursor)

        # Loop through each restaurant and print its href
        for restaurant in restaurants:
            link_element = restaurant.find_element(By.TAG_NAME, "a")  # Assuming each restaurant div has an anchor tag
            href = link_element.get_attribute("href")
            print("Restaurant href:", href)
            fetchDataFromRestaurant(href, cursor, conn, search_text, cities)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the browser after scraping
        driver.quit()