import time

import requests
from bs4 import BeautifulSoup
import csv

from SaveInDB import *


# def getRestaurantURL(restaurant):
#     div = restaurant.find('div', class_='dzrkw9x bzszq0l')
#
#     if div:
#         # Find the <a> tag within this div and get the href attribute
#         link = div.find('a')
#         if link and 'href' in link.attrs:
#             href = link['href']
#             print("Extracted href:", href)
#             return href
#         else:
#             print("Link or href attribute not found")
#             return None
#     else:
#         print("Div not found")
#         return None

#
# def initConnection(url):
#     # Headers to mimic a real browser visit (adjust as needed)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/85.0.4183.121 Safari/537.36 '
#     }
#
#     # Send the request
#     response = requests.get(url, headers=headers)
#
#     # Check if request was successful
#     if response.status_code == 200:
#
#         soup = BeautifulSoup(response.content, "html.parser")
#         #for restaurant in soup.find_all(class_='dzrkw9x bzszq0l'):
#
#         print(soup.prettify())
#
#         test1 = soup.find_all(class_='sc-a874504a-0 jnnveq cb-elevated cb_elevation_elevationXsmall_equ2 au8a0bj r1ad8h3f')   #Thid is not working! just for testing
#         for restaurant in soup.find_all(class_='b1u2igaf'):     #Thid is not working!
#
#             restaurantName = restaurant.find(class_='drxwfi6').get_text(strip=True)
#
#             restaurantURL = getRestaurantURL(restaurant)
#
#             restaurantMenu = fetchDataFromRestaurant(restaurantURL)   #This works!!
#
#
#
#         #url = "https://wolt.com/he/isr/tel-aviv/restaurant/dixie-grill-bar"
#         # "https://wolt.com/he/isr/tel-aviv/restaurant/shake-shack-tlv"




def removeBuzzWordsFromName(name: str):
    name = name.replace("חדש! ", "")
    newName = ''
    for letter in name:
        if u"\u0590" <= letter <= u"\u05EA" or letter.isascii():   #check if its hebrew letter or ascii
            newName += letter
    return newName


def removeSignsFromPrice(price: str):
    newPrice = ''
    for letter in price:
        if letter == ',':
            continue
        if letter == '₪':
            break
        if letter.isascii():
            newPrice += letter

    return float(newPrice)


def checkSpicy(name):
    if '🌶' in name:
        return 1
    return 0


def checkIfRestaurantExists(cursor, resName, cityName, url):
    cursor.execute("""SELECT restaurant_url
                   FROM city_restaurants
                   WHERE restaurant_url=?""",
                   (url,))

    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def removeCityName(name, cities):
    names = name.split('|')
    names = [curr.strip() for curr in names]
    if len(names) == 1:
        return name
    if names[0] in cities:
        return names[1]
    elif names[1] in cities:
        return names[0]
    else:
        return name
    pass


def fetchDataFromRestaurant(url, cursor, conn, cityName, cities):
    # Headers to mimic a real browser visit (adjust as needed)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.121 Safari/537.36 '
    }

    # Send the request
    response = requests.get(url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Define a list to store the menu items
        menu_items = []

        restaurantName = soup.find(class_='h13fol4s').get_text(strip=True)
        restaurantName = removeCityName(restaurantName, cities)
        restaurantNameEnglish = url.split('/')[-1]
        print(f'Restaurant Name: {restaurantName}, In English: {restaurantNameEnglish}')

        if checkIfRestaurantExists(cursor, restaurantName, cityName, url):
            print("Data exists!\n")
            return
        else:
            saveDataInCities(cursor, cityName, restaurantName, restaurantNameEnglish, url)
        restaurant_serial = cursor.lastrowid  # Get the ID of the last inserted row


        for item in soup.find_all(class_='c7e1a2x'):  # Replace with actual class for menu items
            categoryClass = item.find_parent().find_parent().find_parent().find_parent().find(class_='t1rua8h3')
            categoryName = categoryClass.find(class_='hxukhz9').get_text(strip=True)
            name = item.find(class_='tj9ydql').get_text(strip=True)  # Replace with actual class for names
            price = item.find(class_='t11807jm').get_text(strip=True)  # Replace with actual class for prices

            spicy = checkSpicy(name)
            categoryName = removeBuzzWordsFromName(categoryName)
            name = removeBuzzWordsFromName(name)
            price = removeSignsFromPrice(price)
            if price == 0:
                print("Row removed: ", categoryName)
                continue

            #menu_items.append({"category": categoryName, "name": name, "price": price, 'spicy': spicy})
            saveDataInMenu(cursor, restaurant_serial, categoryName, name, price, spicy)
        conn.commit()
        print("Finished!\n")
        #time.sleep(2)  #to prevent Status code: 429 (too much requests to site)
        #return menu_items


    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
        return None
