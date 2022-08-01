from bs4 import BeautifulSoup
import requests
from variable import headersGlobal,root_url



def baca_gambar(url:str):
    'https://komikindo.info/stepmothers-friends-chapter-125/'
    
    image:list[str] #url gambar

    # url = f'https://komikindo.info/stepmothers-friends-chapter-{ke}/'
    r = requests.get(url, headers=headersGlobal)
    bs = BeautifulSoup(r.text, 'lxml')
    
    image = bs.find('div','reader-area').find_all('img')
    image = [x['src'] for x in image]

    return image

def baca_gambar_session(list_url:list):
    list_image:list[list[str]] = []
    
    with requests.Session() as req:
        
        for url in list_url:
            image = []
            r = req.get(url, headers=headersGlobal)
            bs = BeautifulSoup(r.text, 'lxml')
            
            image = bs.find('div','reader-area').find_all('img')
            image = [x['src'] for x in image]
            list_image.append(image)

    return list_image

def baca_gambar_session_async(list_url:list):
    list_image:list[list[str]] = []
    
    with requests.Session() as req:
        
        for url in list_url:
            image = []
            r = req.get(url, headers=headersGlobal)
            bs = BeautifulSoup(r.text, 'lxml')
            
            image = bs.find('div','reader-area').find_all('img')
            image = [x['src'] for x in image]
            list_image.append(image)

    return list_image
