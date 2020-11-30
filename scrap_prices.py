from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

stations = ["Orlen Rakowiecka"] #stations names
stations_url = ["https://pl.fuelo.net/gasstation/id/33701?lang=en"] #stations urls

def ScrapPrice(scrap_url):
	
	uClient = uReq(scrap_url)
	page_html = uClient.read()
	uClient.close()

	page_soup = soup(page_html,"html.parser")

	fuel_types = page_soup.findAll("td",{"itemprop":"name"})
	prices = page_soup.findAll("span",{"itemprop":"price"})
	
	for j in range(len(fuel_types)):
		print(fuel_types[j].text.strip() + ": " + prices[j].text.strip()) #printing prices and types from variables, removing unnecessary spaces

for i in range(len(stations)):

	print("\n" + stations[i])
	
	data = ScrapPrice(stations_url[i])

