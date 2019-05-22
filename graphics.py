#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 02:48:58 2019

@author: kazzastic
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"item-container"})

for container in containers:
    #brand = container.div.div.a.img["title"]
    
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    #print("brand : " +brand)
    print("--|---------------------------|--")
    print("product name : "+product_name)
    print("shipping : "+shipping)
    print("--|---------------------------|--")
    print("\n")
    