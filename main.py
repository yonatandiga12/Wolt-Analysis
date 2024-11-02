from Connection_to_wolt import *
from WoltCityPageLoad import *
from SaveInDB import *













if __name__ == '__main__':
    #get_restaurant_links("https://wolt.com/he/discovery/restaurants", 'הרצליה')

    rest = ['נשר']
    for r in rest:
        get_restaurant_links("https://wolt.com/he/discovery/restaurants", r)
