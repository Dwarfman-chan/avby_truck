from bs4 import BeautifulSoup
import requests
import re

def freightpage():
    url = 'https://truck.av.by/filter?type=2'
    r = requests.get(url=url)

    soup = BeautifulSoup(r.text, "html.parser").form
    req_ads = soup.find('button', class_="button button--secondary button--block")

    total = int(re.sub(r'[^0-9]+', r'', req_ads.text))

    if total % 25 == 0:
        pages = total // 25
    elif total % 25 != 0:
        pages = total // 25 + 1
    
    print(pages)
    return pages