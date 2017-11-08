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

		allLazadaProduct = []

		for container in mainbigcontainer:
			productdiv = container.findAll("div",{"class":"c-product-card__description"})
			pricediv = container.findAll("div",{"class":"c-product-card__price"})
			limitloop = len(productdiv)
			n = 0
			while n!= limitloop:
				productnamelist = productdiv[n].a.text.strip()
				pricetaglist = pricediv[n].span.text.strip()
				allLazadaProduct.append(productnamelist)
				allLazadaProduct.append(pricetaglist)
				n = n + 1
		
		return allLazadaProduct