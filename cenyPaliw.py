from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

stacje = ["Orlen Postępu 16", "Orlen Wołowska", "Shell Al.Wilanowska"]
stacje_url = ["https://pl.fuelo.net/gasstation/id/33683?lang=en", "https://pl.fuelo.net/gasstation/id/32483?lang=en", "https://pl.fuelo.net/gasstation/id/35494?lang=en"]
fuel_type = []
fuel_price = []

#stacja_1
for i in range(len(stacje)):
     my_url = stacje_url[i]

     uClient = uReq(my_url)
     page_html = uClient.read()
     uClient.close()

     page_soup = soup(page_html, "html.parser")

     fuel_name = page_soup.findAll("td", {"itemprop":"name"})
     price = page_soup.findAll("span", {"itemprop" : "price"})
     
     print("")
     print(stacje[i])
     print()
     for pr in price:
          f_price = pr.text
          f_price = f_price.strip()
          fuel_price.append(f_price)
          
          
     for nm in fuel_name:
          f_name = nm.text
          fuel_type.append(f_name)

     for i in range(len(fuel_type)):
          print(fuel_type[i], ": ",fuel_price[i])
     fuel_type = []
     fuel_price = []


