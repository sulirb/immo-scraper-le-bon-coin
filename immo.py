from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json
import os

gecko_driver_path = os.path.join(os.path.dirname(__file__), "./webdriver/geckodriver.exe")
options = webdriver.FirefoxOptions()
options.add_argument('--headless')

options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(service=Service(gecko_driver_path), options=options)

url = 'https://www.leboncoin.fr/recherche?category=9&locations=Paris__48.85749664737371_2.3549660170848816_8109'
driver.get(url)

time.sleep(5)

html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
script_immo = soup.find('script', {'id': '__NEXT_DATA__', 'type': 'application/json'})

if script_immo:
    json_content = script_immo.string 
    with open("immo.json", "w", encoding="utf-8") as f:
        f.write(json_content)
    print("Le contenu JSON a été enregistré dans 'immo.json'")
else:
    print("Le script '__NEXT_DATA__' n'a pas été trouvé.")

driver.quit()

with open("immo.json", "r", encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)
    announces = data["props"]["pageProps"]["searchData"]["ads"]
 
square_values = {}
price_values = {}

for announce in announces:
    announce_id = announce['list_id']
        
    price_values[announce_id] = announce['price_cents'] // 100
    attributes = announce.get("attributes", [])

    for attribute in attributes:
        if isinstance(attribute, dict) and attribute.get('key') == "square":
            square_values[announce_id] = int(attribute['value'])
            break
        
joined_data = {}
for announce_id in square_values.keys():
    if announce_id in price_values:
        joined_data[announce_id] = {
        "m2": square_values[announce_id],
        "prix": price_values[announce_id],
        "prix au m2": price_values[announce_id] // square_values[announce_id]
             }
            
print("Liste des logements:")
print(joined_data)
    
total_square = 0
total_price = 0
for details in joined_data.values():
    total_square += details['m2']
    total_price += details['prix']

print(f"Total m2: {total_square}")
print(f"Total m2: {total_price}")

nbr_houses = len(joined_data)
price_by_square = round(total_price/total_square)
avg_price = round(total_price/len(joined_data))

current_date = datetime.now()

with open("immo.txt", "a",  encoding="utf-8") as f:
    f.write(f"\n{current_date.strftime("%d/%m/%Y, %H:%M")}\n")
    f.write(f"Logements : {nbr_houses}\n")
    f.write(f"Prix moyen du m2 : {price_by_square}\n")
    f.write(f"Prix moyen des logements : {avg_price}\n")
    print("Les articles ont été mis à jour")