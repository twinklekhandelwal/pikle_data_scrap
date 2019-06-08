import requests
from pprint import pprint
import 	json
import os 
import pathlib
url= "https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
url1=requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(url1.text,"html.parser")
main_data=soup.find("div",class_="_1LZ3")
pikal_product=main_data.find("div",class_="_3RA-")
product=main_data.find("div",class_="_1EI9").span.get_text()
index=product.split()
index_data=index[1]
product_number=int(index_data)/32+1
def pikel_data():
    number=1
    pikal_list=[] 
    url_data_store="pikal_data_files/"+"pikal"+str(number)+".json"
    filepath=pathlib.Path(url_data_store)
    if filepath.exists():
        with open(url_data_store,"r") as json_data:
            f=json_data.read()
            f2=json.loads(f)

        return f2
    else:
        
        for j in range(1,product_number+1):
    
            pikal_url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(j)
            url_data=requests.get(pikal_url)
            soup1 = BeautifulSoup(url_data.text,"html.parser")
            main_data1=soup1.find("div",class_="_1LZ3")
            pikal_product1=soup1.find("div",class_="_3RA-")
            data1=pikal_product1.find_all("div",class_="_3WhJ")
            for i in data1:
                pikal_dic={}
                link=i.find("div",class_="_3nWP").get_text()
                name=i.find("div",class_="_2apC").get_text()
                price=i.find("div",class_="_1kMS").get_text()
                pikal_dic["pikal_name"]=name
                pikal_dic["pikal_url"]=url
                pikal_dic["pikal_price"]=price
                pikal_dic["pikal_position"]=number
                number=number+1
                pikal_list.append(pikal_dic)

                url_data_store="pikal_data_files/"+"pikal"+str(number-1)+".json"
                with open(url_data_store,"w") as data:
                    data.write(json.dumps(pikal_dic))
        return pikal_list

pprint(pikel_data())
