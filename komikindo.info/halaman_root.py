from bs4 import BeautifulSoup
import requests
from variable import headersGlobal,root_url

def halaman_root(page=1):
    url = f'https://komikindo.info/page/{page}/' if page > 1 else 'https://komikindo.info/'
    all_card: list[str]
    r = requests.get(url, headers=headersGlobal)
    bs = BeautifulSoup(r.text, "lxml")

    all_card = bs.find('div', 'content').find_all('div', 'flexbox4-content')

    all_card = [
        x.find('a')['href']
        for x in all_card]

    return all_card


if __name__ == '__main__':
    a = halaman_root()
    print(a)
