from bs4 import BeautifulSoup as BS
import requests as r
import pandas as pd
links_to_products=[]
products=[]
prices=[]
url="https://www.olx.pl/motoryzacja/?page="
i=1
url1=url+str(i)
kod = r.get(url1)
doc = BS(kod.text, "html.parser")
how_many_pages=doc.find_all(class_="block br3 brc8 large tdnone lheight24")
how_many_pages=int(how_many_pages[len(how_many_pages)-1].text)
for i in range(1):
    kod = r.get(url1)
    doc = BS(kod.text, "html.parser")
    i=i+1
    url1 = url + str(i)
    strong = doc.find_all("body")
    strong = strong[0].find_all("strong")
    for j in range(len(strong)):
        product=strong[j].parent
        if(product.name=='a'):
            if(product.text!='\n\n\n'):
                products.append((product.text).replace("\n",""))
                links_to_products.append(product['href'])
        if(product.name=='p'):
            if(product.text!='\nWyszukiwanie zostało dodane do obserwowanych\n' and product.text!='\nOgłoszenie dodane do obserwowanych\n'):
                prices.append((product.text).replace("\n",""))

dict={"Nazwa oferty":products,"Link do oferty":links_to_products,"Cena":prices}
df=pd.DataFrame(dict)
df.to_csv('wynik.csv',header=False,index=False)


