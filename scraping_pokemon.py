import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import time
import html.parser
import uuid


headers = {'User-Agent':'Mozilla/5.0'}
driver=webdriver.Chrome("./chromedriver")
baseurl="https://game8.jp/pokemon_sun_moon/87596"

#カウント用
k=0
j=0

pokemons=[]
pokemons_name=[]
#soup2=soup.find_all("ul",id_="mainlist")
#print(soup2)
driver.get(baseurl)
#取り出し
time.sleep(5)
currenturl=driver.current_url
url=requests.get(currenturl)
url.encoding=url.apparent_encoding
soup=BeautifulSoup(url.text,"html.parser")

for pokemon in soup.body.find_all("img",class_="a-img",width="50",height="50",limit=500):
        #driver.find_element_by_class_name('is-next').click()
    print(pokemon.get("src"))
    k+=1
    print(k)
    pokemons.append(pokemon.get("src"))
    pokemons_name.append(pokemon.get("alt"))

#fileに格納
for target in pokemons:
    j+=1
    print(target)
    re=requests.get(target)
    print(str(j)+"/"+str(k))
    with open('pokemon_g1/' + str(pokemons_name[j-1])+str(".jpg"), 'wb') as f:
        f.write(re.content)

print("finish")
driver.close()
