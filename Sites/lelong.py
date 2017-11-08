from bs4 import BeautifulSoup as soup
import requests

class lelongScrapEngine:

	def scrapIt(self, llconcatURL):
		my_url = llconcatURL
		headers = {'User-Agent':'Mozilla/5.0'}
		page = requests.get(my_url)
		page_soup = soup(page.text, "html.parser")

		allLellongProduct = []

		bigcontainer = page_soup.findAll("div",{"class":"item"})
		#productdiv = page_soup.findAll("div",{"class":"summary"})
		#pricediv = page_soup.findAll("span",{"class":"price pull-right"})

		for container in bigcontainer:
			productname = container.findAll("div",{"class":"summary"})
			pricetag = container.findAll("span",{"class":"price pull-right"})
			productnamelist = productname[0].a.text.strip()
			pricetaglist = pricetag[0].b.text.strip()
			allLellongProduct.append(productnamelist)
			allLellongProduct.append(pricetaglist)

		return allLellongProduct
