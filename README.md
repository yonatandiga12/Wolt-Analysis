# Wolt Analysis

View the graphs here: https://yonatandiga12.github.io/Wolt-Analysis/





## Extracting the data

Extracted data from Wolt site, saved in DB and analyzed it.

First I used selenium to enter city name to the input box (it can be done easier by just altering the url of the site, but i wanted to use selenium.

Next I used beautifulsoup to find the name and url of each restaurant.

Then I got inside each restaurant and collected the menu items with their categories.

After each city iteration I scanned the DB to make sure the cities are correct (when ai search tel aviv it can show me restaurant in ramat gan) so it needs to be scanned manually


## Viewing the data

I used Tableau to show some interesting graphs and insights from this data.



## Some Examples:
<br /> 
<br /> 
<p align="center">
  <img src="https://raw.githubusercontent.com/yonatandiga12/Wolt-Analysis/blob/master/Images/Map1.png.jpg" width="1000" title="img1">
</p>
<br /> 
<br /> 
<p align="center">
  <img src="https://raw.githubusercontent.com/yonatandiga12/Wolt_Analysis/master/Images/Branches Counter.jpg" width="1000" title="img2">
</p>
<br /> 
<br /> 
<p align="center">
  <img src="https://raw.githubusercontent.com/yonatandiga12/Wolt_Analysis/master/Images/Branches Dishes.jpg" width="1000" title="img3">
</p>
<br /> 
<br /> 
<p align="center">
  <img src="https://raw.githubusercontent.com/yonatandiga12/Wolt_Analysis/master/Images/Dishes Prices.jpg" width="1000" title="img4">
</p>


### Aditional Info
The data was collected in early November 2024
Got the data from this site: https://wolt.com/he/discovery/restaurants
