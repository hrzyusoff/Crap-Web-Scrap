from urllib.request import urlopen as uReq
# from concatEngine import concatinationEngine
from bs4 import BeautifulSoup as soup

# yeahItIsURL = getScrapURL()

#for category but no need for this time
#catergoryURL = 'Mobile-Phones-and-Gadgets-3020/'
#concatURL = frontMudahURL+catergoryURL+userKeyword+lastMudahURL+fLastMudahURL+userKeyword+sLastMudahURL

class mudahScrapEngine:
	#for loop

	#print(yeahItIsURL)
	def scrapIt(mconcatURL):
		allMudahProduct = []
		userInput = 'noExit'
		while userInput != 'exit':
			userKeyword = input('Enter keyword to search : ')
			frontMudahURL = 'https://www.mudah.my/malaysia/'
			lastMudahURL = '-for-sale'
			fLastMudahURL = '?lst=0&fs=1&w=3&cg=0&q='
			sLastMudahURL = '&so=1&st=s'
			concatURL = frontMudahURL + userKeyword + lastMudahURL + fLastMudahURL + userKeyword + sLastMudahURL
			my_url = concatURL

			#opening up connection, grabbing the page
			uClient = uReq(my_url)
			page_html = uClient.read()
			uClient.close()

			#html parsing
			page_soup = soup(page_html, "html.parser")

			filename = "mudah.csv"
			f = open(filename,"w")
			headers = "Brand, Price\n"
			f.write(headers)

			containers = page_soup.findAll("div",{"class":"top_params_col1"})

			for container in containers:
				brandname = container.h2.a["title"]

				brandprice = container.findAll("div",{"class":"ads_price"})
				brandpricelist = brandprice[0].text.strip()
				allMudahProduct.append(brandname)
				allMudahProduct.append(brandpricelist)
				#print("Brand : "+brandname)
				#print("Price : "+brandpricelist)

				f.write(brandname + "," +brandpricelist+","+"\n")

			f.close()
			return allMudahProduct

