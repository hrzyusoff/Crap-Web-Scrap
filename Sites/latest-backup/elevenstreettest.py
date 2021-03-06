from bs4 import BeautifulSoup as soup
import requests

#url of site to scrap
my_url = 'http://www.11street.my/totalsearch/TotalSearchAction/searchTotal?kwd=asus'
#to act like human that browse from browser
headers = {'User-Agent':'Mozilla/5.0'}
#do requesting to act like human not bot
page = requests.get(my_url)

#html parsing
page_soup = soup(page.text, "html.parser")

maincontainer = page_soup.findAll("div",{"class":"wrap_category"})

allestreetproduct = []

for container in maincontainer:
	n = 0
	productdiv = container.findAll("h3",{"class":"product-name tit_info"})
	pricediv = container.findAll("span",{"class":"rm_price old_price"})
	limitloop = len(productdiv)
	while n != limitloop: 
		productnamelist = productdiv[n].a.text.strip()
		pricetaglist = pricediv[n].text.strip()
		allestreetproduct.append(productnamelist)
		allestreetproduct.append(pricetaglist)
		n = n + 1

print(allestreetproduct)