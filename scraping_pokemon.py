import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver

headers = {'User-Agent':'Mozilla/5.0'}
driver=webdriver.Chrome("./chromedriver")
baseurl="https://zukan.pokemon.co.jp/"
driver.get(baseurl)

#urlを指定、初期化
#baseurl="https://zukan.pokemon.co.jp/"
url=requests.get("https://zukan.pokemon.co.jp/",headers=headers)

#encodingを一致させる
url.encoding=url.apparent_encoding

#決まり文句(soupを初期化
soup=BeautifulSoup(url.content,"lxml")
pokemons=[]

#取り出し
for pokemon in soup.find_all("img",class_="img",limit=500):
     driver.find_element_by_css_selector('#filter_hide_expired').click()
     print(pokemon.get("src"))
     if pokemon.get("src").endswith(".svg"): # imgタグ内の.jpgであるsrcタグを取得
        pokemons.append(pokemon.get("src")) # imagesリストに格納
        #print(pokemons[0])
     elif pokemon.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
        pokemons.append(pokemon.get("src"))
        print(pokemons[1])


#fileに格納
for target in pokemons:
    re=requests.get(requests.compat.urljoin(baseurl,"page/{}".format(target)))
    print("4")
    print(target)
    with open('pokemon_gazou/' + target.split('/')[-1], 'wb') as f:
        f.write(re.content)
if pokemons:
    print("finish")

print("finish")
