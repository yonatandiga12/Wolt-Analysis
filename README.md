# Wolt Analysis

View the graphs: https://yonatandiga12.github.io/Wolt-Analysis/





## Extracting the data

Extracted data from Wolt site, saved in DB and analyzed it.

First I used selenium to enter city name to the input box (it can be done easier by just altering the url of the site, but i wanted to use selenium.

Next I used beautifulsoup to find the name and url of each restaurant.

Then I got inside each restaurant and collected the menu items with their categories.

After each city iteration I scanned the DB to make sure the cities are correct (when ai search tel aviv it can show me restaurant in ramat gan) so it needs to be scanned manually


