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

filename = "card.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)



containers = page_soup.findAll("div", {"class":"item-container"})

for container in containers:
    brand = container.findAll("div", {"class":"item-info"})
    brand_title = brand[0].div.a.img["title"]
    
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    
    print("--|---------------------------|--")
    print("brand : " +brand_title)
    print("product name : "+product_name)
    print("shipping : "+shipping)
    print("--|---------------------------|--")
    print("\n")
    
    
    f.write(brand_title+","+product_name.replace(",", "||")+","+shipping+"\n")
f.close()