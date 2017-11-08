#from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests

my_url ='https://www.instagram.com/explore/tags/sayajual/'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(my_url)

#html parsing
page_soup = soup(page.text, "html.parser")
instacontainers = page_soup.findAll("div",{"class":"_cmdpi"})

for container in phonecontainers:
	phonelist = container.text
	print(phonelist)