from mudah import mudahScrapEngine
from lazada import lazadaScrapEngine

#def getscrapURL(self):
listOfURL = []
userkeyword = input("Enter keyword to search here : ")

#lazada
lazadaMainURL = 'http://www.lazada.com.my/'
lazadaLastURL = '/?searchdirect='
lconcatURL = lazadaMainURL + userkeyword + lazadaLastURL + userkeyword

#mudah
mudahMainURL = 'https://www.mudah.my/malaysia/'
mudahMiddleURL = '-for-sale'
mudahfLastURL = '?lst=0&fs=1&w=3&cg=0&q='
mudahsLastURL = '&so=1&st=s'
mconcatURL = mudahMainURL + userkeyword + mudahMiddleURL + mudahfLastURL + userkeyword + mudahsLastURL

#carousell
carousellMainURL = 'https://carousell.com/search/products/?query='
cconcatURL = carousellMainURL + userkeyword

# listOfURL.append(lconcatURL)
# listOfURL.append(mconcatURL)
# listOfURL.append(cconcatURL)

# print(listOfURL)
#
#
#
displayMResult = mudahScrapEngine()
disp = displayMResult.scrapIt(mconcatURL)
print(disp)
# class concatinationEngine:

# 	#def getscrapURL(self):
# 	listOfURL = []
# 	userkeyword = input("Enter keyword to search here : ")

# 	#lazada
# 	lazadaMainURL = 'http://www.lazada.com.my/'
# 	lazadaLastURL = '/?searchdirect='
# 	lconcatURL = lazadaMainURL + userkeyword + lazadaLastURL + userkeyword

# 	#mudah
# 	mudahMainURL = 'https://www.mudah.my/malaysia/'
# 	mudahMiddleURL = '-for-sale'
# 	mudahfLastURL = '?lst=0&fs=1&w=3&cg=0&q='
# 	mudahsLastURL = '&so=1&st=s'
# 	mconcatURL = mudahMainURL + userkeyword + mudahMiddleURL + mudahfLastURL + userkeyword + mudahsLastURL

# 	#carousell
# 	carousellMainURL = 'https://carousell.com/search/products/?query='
# 	cconcatURL = carousellMainURL + userkeyword

# 	listOfURL.append(lconcatURL,mconcatURL,cconcatURL)

	# def getscrapURL(self):
	# 	return listOfURL

	#return listOfURL
	#print(lconcatURL)
	#print(mconcatURL)
	#print(cconcatURL)