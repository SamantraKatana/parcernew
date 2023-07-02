import requests
import copy
import time
import random
import json


def fetch(url, params):
  try:
    wb_responce = requests.post(url=url, headers=params['headers'])
    print(wb_responce.status_code)
    if len(wb_responce.json()['data']['products']) != 0:
      return wb_responce.json()['data']['products']
    else:
      return False
  except  :
    
    
    
data_products = []
data_products_copy = []
new_products = []
n = 0

while True:
  while True:
    n += 1
    adress_url = str(
        f'https://catalog.wb.ru/catalog/electronic22/catalog?appType=1&curr=rub&dest=-1257786&fbrand=6049&f'
        f'supplier=-100&page={n}&regions=80,38,4,64,83,33,68,70,69,30,86,75,40,1,66,110,22,31,48,71,114&sor'
        f't=popular&spp=0&subject=515')
    responce_data = fetch(adress_url, {
      "headers": {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Referer": str(f"https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?sort="
                       f"popular&page={n}&fbrand=6049&fsupplier=-100"),
        "Referrer-Policy": "no-referrer-when-downgrade"
      },
      "body": None,
      "method": "GET"
    })
    if not responce_data:
      break
    else:
      data_products.extend(responce_data)
    
  if data_products == data_products_copy:
    print("Ничего нового", len(data_products))
  else:
    new_products = [x for x in data_products if x not in data_products_copy]
    count = 0
    for item in new_products:
      count += 1
      print(count)
      print(item["name"])
      print(f'Цвет: {item["colors"][0]["name"]}')
      print(f'Цена: {item["salePriceU"] / 100}    Старая цена:{item["priceU"] / 100}')
      print(f'https://www.wildberries.ru/catalog/{item["id"]}/detail.aspx')
      print()
    data_products_copy = copy.deepcopy(data_products)
  time.sleep(random.randint(20,60))


    
  

    
      
 
        

    

  