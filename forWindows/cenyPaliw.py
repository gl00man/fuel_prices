from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

#tablice
stacje = ["Orlen Postępu 16", "Orlen Wołowska", "Shell Al.Wilanowska", "Circle K Woronicza", "Orlen Hynka 2"]
stacje_url = ["https://pl.fuelo.net/gasstation/id/33683?lang=en", "https://pl.fuelo.net/gasstation/id/32483?lang=en", "https://pl.fuelo.net/gasstation/id/35494?lang=en", "https://pl.fuelo.net/gasstation/id/34690?lang=en", "https://pl.fuelo.net/gasstation/id/33112?lang=en"]
fuel_type = []
fuel_price = []


#google docs
scope = ['https://spreadsheets.google.com/feeds',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]

creds = sac.from_json_keyfile_name('sdd.json', scope)
client = gspread.authorize(creds)
sheet = client.open('fuel_prices').sheet1
z = 1
#petla
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
          #insertRow = [fuel_type[i], fuel_price[i]]
          sheet.update_cell(z, 1, fuel_type[i])
          sheet.update_cell(z, 2, fuel_price[i])
          z = z + 1
     fuel_type = []
     fuel_price = []


