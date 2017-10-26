from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

userInput = 'noExit'
while userInput != 'exit':
	#userCategory = input('Enter category first : ')
	userKeyword = input('Enter keyword to search : ')
	#different things different it lastt code
	catergoryURL = 'Mobile-Phones-and-Gadgets-3020/'
	frontMudahURL = 'https://www.mudah.my/malaysia/'
	#middleMudahURL = userKeyword
	lastMudahURL = '-for-sale'
	fLastMudahURL = '?lst=0&fs=1&w=3&cg=3020&q='
	sLastMudahURL = '&so=1&st=s'
	concatURL = frontMudahURL+catergoryURL+userKeyword+lastMudahURL+fLastMudahURL+userKeyword+sLastMudahURL
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

		print("Brand : "+brandname)
		print("Price : "+brandpricelist)

		f.write(brandname + "," +brandpricelist+","+"\n")

	f.close()

#userInput('Continue to search : ')

