from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import random
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

Text = ""
driver = webdriver.Firefox()
# driver.get('http://localhost')
driver.fullscreen_window()
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
zoomsite = "https://www.zoocasa.com/search?attached=false&condo=false&latitude=45.18572493688514&longitude=-75.8498306274414&price-max=800000&semidetached=false&zoom=12"
# zoomsite2 = "https://www.zoocasa.com/search?attached=false&amp;condo=false&amp;latitude=45.18572494033834&amp;longitude=-75.8498306274414&amp;price-max=800000&amp;semidetached=false&amp;zoom=12&amp;page=2"
rew = "https://www.rew.ca/properties/map?lat=45.111815521121336&lng=-75.89063644409181&zoom=12&bounds%5Bsw%5D%5Blat%5D=45.00535038430806&bounds%5Bsw%5D%5Blng%5D=-76.16615295410158&bounds%5Bne%5D%5Blat%5D=45.21808242410029&bounds%5Bne%5D%5Blng%5D=-75.61511993408205&sort=featured&direction=desc&page=1&isExactBathrooms=false&isExactBedrooms=false&numBedrooms=0%2B&numBathrooms=0%2B&priceFrom=&priceTo=&sqftFrom=&sqftTo=&yearBuiltFrom=&yearBuiltTo=&keywords=&propertyTypes=&openHouseOnly=false"
#     'price': '',
#     'street': '',
#     'details': '',
#     'sqft': '',
#     'date': ''
# }
db = {'zoomcasa': []}


def zoomquery():
    _list = []
    _listings = []
    driver.get(zoomsite)
    n = random.uniform(7.0, 10.0)
    WebDriverWait(driver, int(n))
    # WebDriverWait(driver, int(n)).until(
    #     EC.visibility_of_element_located(
    #         (By.XPATH, "/html/body/div[3]/div/div/div[2]/section/div/item-group/loading-data/pagination-nav/a[2]")))

    ad = float
    ad = n + 1.0
    time.sleep(ad)
    html = driver.page_source
    _list.append(html)

    # db['zoomcasa'].append(html)

    # print(f'Difference: {False if html == snap else True}')
    # print(html)
    # soup = BeautifulSoup(html, 'html.parser')
    # try:
    #     # test = substract(html, snap)
    #     testsoup = BeautifulSoup(test, 'html.parser')
    #     print(testsoup.text)
    #     listings = testsoup.findAll("div", {"class": "card-wrapper"})
    #     db['zoomcasa'] = listings
    # except Exception as e:
    #     print(e.args, e.__str__())
    #     raise e

    # print(soup)
    # dvs = soup.findAll("div", {"class": "card-wrapper"})
    # pages = []
    # pages.append(dvs)
    # driver.get
    def next_click(try_it: bool):
        while try_it:
            try:
                n = random.uniform(4.0, 6.0)
                WebDriverWait(driver, int(n)).until(
                    EC.visibility_of_element_located((By.XPATH,
                                                      "/html/body/div[3]/div/div/div[2]/section/div/item-group/loading-data/pagination-nav/a[2]")))
                my_link = driver.find_element_by_xpath(
                    "/html/body/div[3]/div/div/div[2]/section/div/item-group/loading-data/pagination-nav/a[2]")
                if my_link.get_attribute("class") == "icon-arrow-right-open active":
                    my_link.click()
                    # n = random.uniform(4.0, 6.0)
                    time.sleep(n + 1.0)
                    WebDriverWait(driver, int(n)).until(
                        EC.visibility_of_element_located((By.XPATH,
                                                          "/html/body/div[3]/div/div/div[2]/section/div/item-group/loading-data/pagination-nav/a[2]")))
                    _list.append(driver.page_source)
                else:
                    try_it = False
            except Exception as e:
                print(e.args, e.__str__())
                raise e
                try_it = False

    next_click(try_it=True)
    for l in _list:
        soup = BeautifulSoup(l, 'html.parser')
        listings = soup.findAll("div", {"class": "card-wrapper"})
        # print(_list)

        for house in listings:
            try:
                listing = {
                    'price': '',
                    'street': '',
                    'details': '',
                    'sqft': '',
                    'date': ''
                }

                price = house.find("div", {"class": "price"})
                price = price.text
                listing['price'] = price.strip()

                street = house.find("div", {"class": "street"})
                street = street.text
                listing['street'] = street.strip()

                details = house.find("div", {"class": "details"})
                details = details.text
                listing['details'] = details.strip()

                sqft = house.find("div", {"class": "sqft"})
                sqft = sqft.text
                listing['sqft'] = sqft.strip()

                date = house.find("div", {"class": "date"})
                date = date.text
                listing['date'] = date.strip()

                db['zoomcasa'].append(listing)

            except AttributeError:
                continue


def realquery():
    _list = []
    _listings = []
    time.sleep(3.5)
    driver.get(rew)
    n = random.uniform(7.0, 10.0)
    WebDriverWait(driver, int(n))
    # WebDriverWait(driver, int(n)).until(
    #     EC.visibility_of_element_located(
    #         (By.XPATH, "/html/body/div[3]/div/div/div[2]/section/div/item-group/loading-data/pagination-nav/a[2]")))

    ad = float
    ad = n + 1.0
    time.sleep(ad)
    # input("Press Enter to continue...")
    html = driver.page_source

    _list.append(html)

    # db['zoomcasa'].append(html)

    # print(f'Difference: {False if html == snap else True}')
    # print(html)
    # soup = BeautifulSoup(html, 'html.parser')
    # try:
    #     # test = substract(html, snap)
    #     testsoup = BeautifulSoup(test, 'html.parser')
    #     print(testsoup.text)
    #     listings = testsoup.findAll("div", {"class": "card-wrapper"})
    #     db['zoomcasa'] = listings
    # except Exception as e:
    #     print(e.args, e.__str__())
    #     raise e

    # print(soup)
    # dvs = soup.findAll("div", {"class": "card-wrapper"})
    # pages = []
    # pages.append(dvs)
    # driver.get
    def next_click(try_it: bool):
        while try_it:
            try:
                n = random.uniform(7.5, 10.0)
                WebDriverWait(driver, int(n)).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "/html/body/form/div[2]/section[2]/div[3]/article[1]/footer/a")))
                my_link = driver.find_element_by_xpath("/html/body/form/div[2]/section[2]/footer/a[2]")
                if my_link.get_attribute("class") == "mappagination-next is-disabled":
                    break
                if my_link.get_attribute("class") == "mappagination-next":
                    my_link.click()
                    # n = random.uniform(4.0, 6.0)
                    time.sleep(n + 1.0)
                    WebDriverWait(driver, int(n)).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "/html/body/form/div[2]/section[2]/div[3]/article[1]/footer/a")))
                    _list.append(driver.page_source)
                else:
                    try_it = False
            except Exception as e:
                print(e.args, e.__str__())
                raise e
                try_it = False

    next_click(try_it=True)

    for l in _list:
        soup = BeautifulSoup(l, 'html.parser')
        listings = soup.findAll("article", {"class": "propertycard"})
        # print(_list)

        for house in listings:
            try:
                listing = {
                    'price': '',
                    'street': '',
                    'details': '',
                }

                price = house.find("div", {"class": "propertycard-price"})
                price = price.text
                listing['price'] = price.strip()

                street = house.find("a", {"class": "propertycard-address"})
                street = street.text
                listing['street'] = street.strip()

                details = house.find("ul", {"class": "propertycard-attributes"})
                details = details.text
                listing['details'] = details.strip()

                # sqft = house.find("div", {"class": "sqft"})
                # sqft = sqft.text
                # listing['sqft'] = sqft.strip()
                #
                # date = house.find("div", {"class": "date"})
                # date = date.text
                # listing['date'] = date.strip()

                db['zoomcasa'].append(listing)

            except AttributeError:
                continue


def homebase():
    # zoomquery()
    realquery()
    n = random.uniform(5.0, 7.0)
    time.sleep(n)


homebase()

# elems = soup.find_elements_by_class_name("card-wrapper")
# for elem in elems:
# links = div.find_elements_by_css_selector("listing-card")
# send = driver.find_element_by_name("send")
# print(send)

# n = random.uniform(1.5 , 5.0)
# print(n)
# time.sleep(n)

# elem.send_keys('test')

# send.click()
##element_present = EC.presence_of_element_located((By.ID, 'element_id'))
##WebDriverWait(driver, timeout).until(element_present)
#
# div = driver.find_element_by_tag_name('form')
#
#
#
# # [link.find('h3').text for l in links ]
# for link in links:
#     print (link.text)
#
# n = random.uniform(1.0,3.0)
# print (n)
# time.sleep(n)
#
# print ("all done")


# query()

driver.quit()

##elem.send_keys(user)
##elem = driver.find_element_by_id("pass")
##elem.send_keys(pwd)
##elem.send_keys(Keys.RETURN)



