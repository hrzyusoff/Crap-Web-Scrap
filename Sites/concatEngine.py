from mudah import mudahScrapEngine
from lazada import lazadaScrapEngine
from elevenstreet import estreetScrapEngine
# from carousell import carousellScrapEngine
from lelong import lelongScrapEngine

userInput = 'noExit'
while userInput != 'exit':
	#def getscrapURL(self):
	#listOfURL = []
	userkeyword = input("\nEnter keyword to search here : ")

	#lazada
	lazadaMainURL = 'http://www.lazada.com.my/'
	lazadaLastURL = '/?itemperpage=60&sc=MS0F&searchredirect='
	lconcatURL = lazadaMainURL + userkeyword + lazadaLastURL + userkeyword

	#mudah
	mudahMainURL = 'https://www.mudah.my/malaysia/'
	mudahMiddleURL = '-for-sale'
	mudahfLastURL = '?lst=0&fs=1&w=3&cg=0&q='
	mudahsLastURL = '&so=1&st=s'
	mconcatURL = mudahMainURL + userkeyword + mudahMiddleURL + mudahfLastURL + userkeyword + mudahsLastURL

	#elevenstreet
	elevenstreetMainURL = 'http://www.11street.my/totalsearch/TotalSearchAction/searchTotal?kwd='
	esconcatURL = elevenstreetMainURL + userkeyword

	#lelong
	lelongMainURL = 'https://www.lelong.com.my/catalog/all/list?TheKeyword='
	llconcatURL = lelongMainURL + userkeyword

	#carousell
	# carousellMainURL = 'https://carousell.com/search/products/?query='
	# cconcatURL = carousellMainURL + userkeyword

	scrapMudahResult = mudahScrapEngine()
	displayMudahResult = scrapMudahResult.scrapIt(mconcatURL)

	scrapLazadaResult = lazadaScrapEngine()
	displayLazadaResult = scrapLazadaResult.scrapIt(lconcatURL)

	scrapLelongResult = lelongScrapEngine()
	displayLelongResult = scrapLelongResult.scrapIt(llconcatURL)

	scrapElevenstreetResult = estreetScrapEngine()
	displayEstreetResult = scrapElevenstreetResult.scrapIt(esconcatURL)

	# scrapCarousellResult = carousellScrapEngine()
	# displayCarousellResult = scrapCarousellResult.scrapIt(cconcatURL)

	print("\nThis is result from MUDAH Website : \n\n",displayMudahResult)
	print("\n\nThis is result from LAZADA Wesbite : \n\n",displayLazadaResult)
	print("\n\nThis is result from LELONG Wesbite : \n\n",displayLelongResult)
	print("\n\nThis is result from ELEVEN STREET Wesbite : \n\n",displayEstreetResult)
	# print("\n\nThis is result from CAROUSELL Wesbite : \n\n",displayCarousellResult)	

