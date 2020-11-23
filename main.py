import time
import pandas as pd
from immo_db import *
from link_pages import explore_page

import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#Creating an empty database using the function create_db()
immo_db = create_db()

#Setting up the webdriver to access selenium
options = Options()
options.headless = True
driver = webdriver.Firefox()

#Extracting data from the pages of "immoweb.be"
for p in range(300):
    
    #To access the right page, we need to increase p by 1
    p += 1
    
    #For the first page, the url is slightly different
    if p == 1:
        
        url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE"
        immo_db = explore_page(url, immo_db, driver)
       
    #For the other pages, we just need to change the p value
    else:
        time.sleep(5)
        url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE&page={}&orderBy=relevance".format(p)
        immo_db = explore_page(url, immo_db, driver)


#Same as above except we extract property for rent
'''
for p in range(7):
    
    #To access the right page, we need to increase p by 1
    p += 1
    
    #For the first page, the url is slightly different
    if p == 1:
        
        url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-louer?countries=BE"
        immo_db = explore_page(url, immo_db, driver)
       
    #For the other pages, we just need to change p value
    else:
        
        url = "https://www.immoweb.be/fr/recherche/maison-et-appartement/a-louer?countries=BE&page={}&orderBy=relevance".format(p)
        immo_db = explore_page(url, immo_db, driver)

'''
print(immo_db)


#exporting the csv file

immo_db.to_csv(r"C:\Users\mah83\Documents\GitHub\challenge-collecting-data\data300pages.csv", index=False)
  





