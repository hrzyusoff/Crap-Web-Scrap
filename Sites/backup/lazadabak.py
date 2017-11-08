from bs4 import BeautifulSoup as soup
# from concatEngine import concatinationEngine
import requests

# yeahItIsURL = getScrapURL()

class lazadaScrapEngine:
	#url of site to scrap
	my_url ='http://www.lazada.com.my/shop-women-hijabs/?q=tudung&searchredirect=tudung'
	#to act like human that browse from browser
	headers = {'User-Agent':'Mozilla/5.0'}
	#do requesting to act like human not bot
	page = requests.get(my_url)

	#html parsing
	page_soup = soup(page.text, "html.parser")
	#crawling into element in html

	productdiv = page_soup.findAll("div",{"class":"c-product-card__description"})
	productaddr = page_soup.findAll("a",{"class":"c-product-card__name"})

	pricediv = page_soup.findAll("div",{"class":"c-product-card__price"})
	pricespan = page_soup.findAll("span",{"class":"c-product-card__price-final"})

	#smallcontainers = page_soup.findAll('div',{"class":'c-product-card c-product-list__item   c-product-card_view_grid new_ outofstock installments_1  c-product-card_js_inited'})
	bigcontainer = page_soup.findAll("div",{"class","c-product-list  c-product-list_view_grid c-product-list_justify_space-between c-catalog-controller__product-list c-product-list_js_inited"})
	
	lengthA = len(productaddr)
	print(lengthA)

	allOfProduct = []

	for container in productaddr:
		productname = container.text.strip()
		allOfProduct.append(productname)

	print(allOfProduct)

	# for container in pricespan:
	# 	productprice = container.text.strip()
	# 	print(productprice)
