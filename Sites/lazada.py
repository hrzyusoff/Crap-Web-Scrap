#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

my_url ='http://www.lazada.com.my/shop-mobiles/apple/?searchredirect=iphone'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(my_url)

#html parsing
page_soup = soup(page.text, "html.parser")
phone = page_soup.findAll("a",{"class":"c-product-card__name"})

print(phone)