# Collect data from [Immoweb](http://www.immoweb.be/ "Title")

![Texte alternatif](https://blog.immoweb.be/app/uploads/2019/08/immoweb-full-logo.jpg" )


#### BeCode challenge: from 18/11/20 to 23/11/20

#### Contributors: Guillaume, Reza, Frédéric

## Aim of this project

- Scraping real estate website pages (application to the immoweb website)
- The output is  a csv file with at least 10,000 properties and a list of features (see below)

## Tools 

- Using tools such as [Selenium](https://selenium-python.readthedocs.io/ "Title") and [Pandas](https://pandas.pydata.org/ "Title") in Python

## Description of the files 

The code is divided in 4 files:

- *main.py*: this file needs to be run in order to extract the properties. It calls different functions that are built in the other files (see below)
  in order to create the dataframe, extract the features of the properties and put them in the same dataframe. 
  
   We need to specify in this file:

  - the range of pages extracted at once from [Immoweb](https://www.immoweb.be/fr/recherche/maison-et-appartement/a-vendre?countries=BE "Title")
  - the csv file where the extracted data are stored
  
  
- *immo_db.py*: this file contains the functions needed to create the database and fill it with data

- *link_pages.py*: this function contains the function *explore_page* which is called by *main.py* to collect a first set of features of a given property: 

  - Its locality
  - Its postal code
  - Its price
  - If the property has already been built

  This function also collects the url-link of a given property in order to extract the rest of the features. 
  Once all the features are gathered, *explore_page* also adds the data in the pandas dataframe created in *main.py*. 

- *link_values.py*: this file contains the function *get_info_prop*, its goal is to extract the following info from a page:

  - Number of rooms
  - If there is a equiped kitchen
  - If there is a terasse and its area
  - If there is a garden and its area
  - The livable area
  - If the property furnished
  - If there is an open fire
  - The number of facades
  - If there is a pool
  - The state of the property
 
 All of these features are then returned to the *explore_page* function. 

## Simulation results
We scraped 334 pages of selling properties and 7 pages of renting properties and reached **10,201** properties.
The csv file can be found in this repository as **immoweb_database.csv**


## Libraries used

- [Pandas](https://pandas.pydata.org/ "Title")
- [ReGex](https://docs.python.org/3/library/re.html "Title")
- [Selenium](https://selenium-python.readthedocs.io/ "Title")
- [Selenium Webdriver](https://selenium-python.readthedocs.io/api.html "Title")
- [Selenium Keys](https://selenium-python.readthedocs.io/ "Title")
- [Selenium Options](https://selenium-python.readthedocs.io/ "Title")
- [Time](https://docs.python.org/3/library/time.html "Title")




![Texte alternatif](https://www.wynnandwynn.com/wp-content/uploads/2016/12/real-estate.jpg" )
