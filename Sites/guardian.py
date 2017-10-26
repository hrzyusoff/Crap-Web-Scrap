#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

my_url ='https://guardian.com.my/index.php/catalogsearch/result/?q=Tissue'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(my_url)

#html parsing
page_soup = soup(page.text, "html.parser")
phone = page_soup.findAll("a",{"class":"c-product-card__name"})

print(phone)