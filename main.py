from Connection_to_wolt import *
from WoltCityPageLoad import *
from SaveInDB import *













if __name__ == '__main__':
    #get_restaurant_links("https://wolt.com/he/discovery/restaurants", 'הרצליה')

    #rest = ['שדרות', 'באר יעקב', 'טירת כרמל', 'כפר יונה', 'מגדל העמק' , 'קריית מלאכי','יקנעם עילית' ,'נשר']
    rest = ['קריית ביאליק', 'נוף הגליל' , 'קריית מוצקין', 'קריית ים','צפת','קריית שמונה']
    for r in rest:
        get_restaurant_links("https://wolt.com/he/discovery/restaurants", r)
