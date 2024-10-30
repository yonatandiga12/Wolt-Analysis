import sqlite3




def init_database(db_name="restaurants.db"):
    """
    Initializes the SQLite database and creates the necessary tables.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create city_restaurants table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS city_restaurants (
            city TEXT,
            restaurant_serial INTEGER PRIMARY KEY,
            restaurant_name TEXT,
            restaurant_name_english TEXT,
            restaurant_url TEXT
        )
    ''')

    # Create restaurant_menus table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurant_menus (
            restaurant_serial INTEGER,
            category_name TEXT,
            dish_name TEXT,
            price FLOAT,
            spicy INTEGER,
            FOREIGN KEY (restaurant_serial) REFERENCES city_restaurants (restaurant_serial)
        )
    ''')

    conn.commit()
    #conn.close()

    return cursor, conn


def saveDataInCities(cursor, cityName, restaurantName, restaurantNameEnglish, url):
    cursor.execute('''
                    INSERT INTO city_restaurants (city, restaurant_name, restaurant_name_english, restaurant_url) 
                    VALUES (?, ?, ?, ?)
                ''', (cityName, restaurantName, restaurantNameEnglish, url))

def saveDataInMenu(cursor, restaurant_serial, category_name, dish_name, price, spicy):
    # Insert menu item into restaurant_menus
    cursor.execute('''
            INSERT INTO restaurant_menus (restaurant_serial, category_name, dish_name, price, spicy)
            VALUES (?, ?, ?, ?, ?)
        ''', (restaurant_serial, category_name, dish_name, price, spicy))


