import pandas as pd
import time
from colors import *



print(f"{CYAN}                         ....::::  {RESET}")
print(f"{YELLOW} ¤ # ¤ # ¤ # ¤ # ¤ # ¤ # ¤ # ¤ # ¤ {RESET}")                     
print(f"{GREEN}     _____     _  {CYAN}!!. .:.....{RESET}")
print(f"{GREEN}    | __  |___| |_ ___ ___ ___     {RESET}")
print(f"{GREEN}    | __ -| . |  _|   | -_|   |    {RESET}")
print(f"{GREEN}    |_____|___|_| |_|_|___|_|_|    {RESET}")
print(f"{CYAN}__..;--..._                        {RESET}")
print(f"{YELLOW} ¤ # ¤ # ¤ # ¤ # ¤ # ¤ # ¤ # ¤ # ¤ {RESET}")
print(f"{WHITE}\nWelcome to BOTnen Price scraping\nYour scraping in underway...\n\n{RESET}")
time.sleep(2)

print(f"Scraping the following stores:{BRIGHT_BLUE}\n- REMA1000\n- KIWI\n- MENY\n- SPAR\n- Bunnpris\n- CoopExtra\n- CoopPrix\n- Joker\n\n{RESET}")

time.sleep(1)

import scraper_bunnpris
import scraper_kiwi
import scraper_MENY
import scraper_rema1000
import scraper_coop_extra
import scraper_spar
import scraper_coop_prix
import scraper_joker
def scrape_deals():
    deals = []

    print(f'{CYAN}\n\nREMA1000{RESET}')
    deals.extend(scraper_rema1000.get_deals())
    print(f'{YELLOW}\n\nKIWI{RESET}')
    deals.extend(scraper_kiwi.get_deals())
    print(f'{CYAN}\n\nMENY{RESET}')
    deals.extend(scraper_MENY.get_deals())
    print(f'{YELLOW}\n\nSPAR{RESET}')
    deals.extend(scraper_spar.get_deals())
    print(f'{CYAN}\n\nBUNNPRIS{RESET}')
    deals.extend(scraper_bunnpris.get_deals())
    print(f'{YELLOW}\n\nCOOP EXTRA{RESET}')
    deals.extend(scraper_coop_extra.get_deals())
    print(f'{CYAN}\n\nCOOP Prix{RESET}')
    deals.extend(scraper_coop_prix.get_deals())
    print(f'{YELLOW}\n\nJOKER{RESET}')
    deals.extend(scraper_joker.get_deals())
    
    

    df = pd.DataFrame(deals)

    df.to_csv('deals.csv', index=False)
    df.to_excel('deals.xlsx', index=False)
    return deals 