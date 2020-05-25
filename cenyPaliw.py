from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

stacje = ["Orlen Postępu 16", "Orlen Wołowska", "Shell Al.Wilanowska"]
stacje_url = ["https://pl.fuelo.net/gasstation/id/33683?lang=en", "https://pl.fuelo.net/gasstation/id/32483?lang=en", "https://pl.fuelo.net/gasstation/id/35494?lang=en"]
rodzaje_paliw_orlen = ["EFFECTA 95","EFFECTA DIESEL", "LPG", "VERVA98", "VERVA ON" ]
rodzaje_paliw_shell = ["FuelSave 95", "FuelSave Diesel", "V-Power Nitro+ Racing", "V-Power Nitro+ Diesel"]

#stacja_1
for i in range(len(stacje)):
     my_url = stacje_url[i]

     uClient = uReq(my_url)
     page_html = uClient.read()
     uClient.close()

     page_soup = soup(page_html, "html.parser")

     con = page_soup.findAll("span", {"itemprop" : "price"})
     print("")
     print(stacje[i])
     print()
     i = 0
     for p in con:
          a = p.text
          if(i == 2):
               print(rodzaje_paliw_shell[i], ": ", a.strip())
          else: 
               print(rodzaje_paliw_orlen[i], ": ", a.strip())
          
          i = i + 1

