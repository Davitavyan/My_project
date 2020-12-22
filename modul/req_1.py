import requests
from bs4 import BeautifulSoup
url="http://httpbin.org/xml"
res=requests.get(url)
print(res)
print('----'*10)
url1="http://httpbin.org/get"
res2=requests.get(url1,{"key1":1,"key2":'two',"key3":False})
soup=BeautifulSoup(res2.text,'html.parser')
print("text",res2.text)
print('----'*20)
print("url",res2.url)
print("status_code",res2.status_code)
print('----'*10)
url3='http://quotes.toscrape.com/'
res3=requests.get(url3)
soup=BeautifulSoup(res3.text,'html.parser')
quotes=soup.find_all("span",class_='text')
for quote in quotes:
    print(quote.text)
    print('-------')
print('----'*10)
import json
import requests

js = requests.get ('https://httpbin.org/json')

print(js.json())
