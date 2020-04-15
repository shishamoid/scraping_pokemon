import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import time

headers = {'User-Agent':'Mozilla/5.0'}
driver=webdriver.Chrome("./chromedriver")
baseurl="https://zukan.pokemon.co.jp/"

#スクロール

driver.get(baseurl)
for i in range(1,10):
    time.sleep(3)
    currenturl=driver.current_url
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    if i==6:
        url=requests.get(currenturl)
        break


url.encoding=url.apparent_encoding


soup=BeautifulSoup(url.text,"lxml")
pokemons=[]
#soup2=soup.find_all("ul",id_="mainlist")
#print(soup2)

#取り出し
for pokemon in soup.main.find_all("img",class_="img",limit=500):
    print(pokemon)
    print(pokemon.get("src"))
    if pokemon.get("src").endswith(".img"): # imgタグ内の.jpgであるsrcタグを取得
        pokemons.append(pokemon.get("src")) # imagesリストに格納
        #print(pokemons[0])
    elif pokemon.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
            pokemons.append(pokemon.get("src"))
            print(pokemons[1])



#fileに格納
for target in pokemons:
    re=requests.get(requests.compat.urljoin(currenturl,"page/{}".format(target)))
    print("4")
    print(target)
    with open('pokemon_gazou/' + target.split('/')[-1], 'wb') as f:
        f.write(re.content)

if pokemons:
    print("finish")


print("finish")
