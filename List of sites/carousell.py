from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

userInput = 'noExit'
while userInput != 'exit':
	#userCategory = input('Enter category first : ')
	#userKeyword = input('Enter keyword to search : ')
	#frontMudahURL = 'https://shopee.com.my/search/?keyword=iphone'
	#concatURL = frontMudahURL+userKeyword
	my_url = 'https://carousell.com/search/products/?query=iphone'

	#opening up connection, grabbing the page
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	#html parsing
	page_soup = soup(page_html, "html.parser")

	#filename = "mudah.csv"
	#f = open(filename,"w")
	#headers = "Brand, Price\n"
	#f.write(headers)

	containers = page_soup.findAll("div",{"class":"row card-row"})

	for container in containers:
		brandname = container.div.findAll("div",{"class":"ProductCard__cardTitleContent___LESPy"})

		brandprice = container.div.findAll("div",{"class":"ProductCard__cardTitleContent___LESPy"})
		brandpricelist = brandprice[0].text.strip()

		print("Brand : "+brandname)
		print("Price : "+brandpricelist)

		#f.write(brandname + "," +brandpricelist+","+"\n")

	#f.close()

#userInput('Continue to search : ')

#find('h1',attrs={'itemprop':'name'})