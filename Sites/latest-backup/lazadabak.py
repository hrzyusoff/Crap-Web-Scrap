from bs4 import BeautifulSoup as soup
import requests

class lazadaScrapEngine:
	
	def scrapIt(self, lconcatURL):
		#url of site to scrap
		my_url = lconcatURL
		#to act like human that browse from browser
		headers = {'User-Agent':'Mozilla/5.0'}
		#do requesting to act like human not bot
		page = requests.get(my_url)

		#html parsing
		page_soup = soup(page.text, "html.parser")
		#main container including header
		mainbigcontainer = page_soup.findAll("div",{"class":"catalog__main__content"})
		#main container, item only
		#bigcontainer = page_soup.findAll("div",{"class":"c-product-list  c-product-list_view_grid c-product-list_justify_space-between c-catalog-controller__product-list c-product-list_js_inited"})
		#specific container terus
		#sdetailcontainer = page_soup.findAll("div",{"class":"c-product-card c-product-list__item   c-product-card_view_grid new_ outofstock installments_  c-product-card_js_inited"})
		allLazadaProduct = []

		for container in mainbigcontainer:
			productdiv = container.findAll("div",{"class":"c-product-card__description"})
			pricediv = container.findAll("div",{"class":"c-product-card__price"})
			limitloop = len(productdiv)
			n = 0
			while n!= limitloop:
				productname = productdiv[n].a.text.strip()
				pricename = pricediv[n].span.text.strip()
				allLazadaProduct.append(productname)
				allLazadaProduct.append(pricename)
				n = n + 1
		
		return allLazadaProduct
		
		# #crawling into element in html
		# productdiv = page_soup.findAll("div",{"class":"c-product-card__description"})
		# productaddr = page_soup.findAll("a",{"class":"c-product-card__name"})

		# pricediv = page_soup.findAll("div",{"class":"c-product-card__price"})
		# pricespan = page_soup.findAll("span",{"class":"c-product-card__price-final"})

		# bigcontainer = page_soup.findAll("div",{"class","c-product-list  c-product-list_view_grid c-product-list_justify_space-between c-catalog-controller__product-list c-product-list_js_inited"})

		# allLazadaProduct = []

		# for container in bigcontainer:
		# 	productname = container.findAll("div",{"class":"c-product-card__description"})
		# 	productnameaddr = productname.findAll("a",{"class":"c-product-card__name"})

		# for container in productaddr:
		# 	productname = container.text.strip()
		# 	allLazadaProduct.append(productname)

		# for container in pricespan:
		# 	productprice = container.text.strip()
		# 	allLazadaProduct.append(productprice)

		# return allLazadaProduct