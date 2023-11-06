from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from colors import *

chrome_options = Options()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)

butikk_navn = 'REMA-1000'

print(f'Scraping {butikk_navn}\nPlease wait...\n')

def get_deals():
    url = 'https://etilbudsavis.no/'+(str(butikk_navn))+'/tilbud'
    driver.get(url)


    for i in range(10):  
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
        time.sleep(2)  

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    driver.quit()

    offers = soup.find_all('a', class_='OfferList__OfferListItemLink-sc-bj82vg-3')
    deals = []

    for offer in offers:
        title = offer.find('header', itemprop='name').get_text(strip=True) if offer.find('header', itemprop='name') else 'No Title'
        price_info = offer.select_one('.OfferList__OfferPcs-sc-bj82vg-7') 
        price_per_unit = price_info.get_text(strip=True) if price_info else 'No Price per Unit'
        price_tag = offer.select_one('.OfferList___StyledSpan2-sc-bj82vg-14')
        price = price_tag.get_text(strip=True) if price_tag else 'No Price'
            
        deals.append({
            'store': butikk_navn,
            'title': title,
            'price_per_unit': price_per_unit,
            'price': price,
        })

    for deal in deals:
        print(f"{RED}Store{RESET}: {butikk_navn}")
        print(f"{RED}Title{RESET}: {deal['title']}")
        print(f"{RED}Price per unit{RESET}: {deal['price_per_unit']}")
        print(f"{RED}Price{RESET}: {deal['price']}")
        print('---------------')
        
    return deals