#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

class carousellScrapEngine:
	my_url  = 'https://carousell.com/search/products/?query=iphone'

	#headers used to treat like human request 
	#not using urllib because  it is like treat of bot
	headers = {'User-Agent':'Mozilla/5.0'}
	page = requests.get(my_url)

	#html parsing
	page_soup = soup(page.text, "html.parser")

# containers = page_soup.findAll("div",{"class":"row card-row"})
# for container in containers:
# 	brandname = container.findAll("h4",{"class":"ProductCard__cardTitleContent___LESPy"})
# 	brandnamelist = brandname[0].text
# 	brandprice = container.findAll("span",{"class":"ProductCard__cardPrice___1b7Lt"})
# 	brandpricelist = brandprice[0].text
# 	print("Brand : "+brandnamelist)
# 	print("Price : "+brandpricelist)

	# #jadi tapi tak sekali
	#containers = page_soup.findAll("div",{"class":"row card-row"})
	gadgetname_h4 = page_soup.findAll("h4",{"class":"ProductCard__cardTitleContent___LESPy"})
	for container in gadgetname_h4:
		namelist = container.text
		print(namelist)

	gadgetprice_span = page_soup.findAll("span",{"class":"ProductCard__cardPrice___1b7Lt"})
	for container in gadgetprice_span:
		pricelist = container["title"]
		print(pricelist)

# #for container in containers:
# 	#gadgetname = page_soup.findAll("h4",{"class":"ProductCard__cardTitleContent___LESPy"})
# 	#gadgetprice = container.findAll("span",{"class":"ProductCard__cardPrice___1b7Lt"})
# 	#print(gadgetname)
# 	#print(gadgetprice)