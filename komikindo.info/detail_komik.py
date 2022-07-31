import re
from bs4 import BeautifulSoup
import requests
from data_class.Komik import Komik
from data_class.Chapter import Chapter
from variable import headersGlobal, root_url


def get_genre(bs: BeautifulSoup):
    try:
        genre = bs.find('div', 'series-genres').find_all('a')
        genre = [x.get_text(strip=True).lower() for x in genre]
        return genre
    except:
        return []


def get_list_chapter(bs: BeautifulSoup):
    ch = bs.find('ul', 'series-chapterlist').find_all('li')
    ch = [{
        'href': x.find('div', 'flexch-infoz').find('a')['href'],
        'ke': x.find('div', 'flexch-infoz').find('span').get_text(strip=True).lower().replace('chapter', '').strip()
    }
        for x in ch]
    ch.reverse()
    return ch


def detail(url: str):
    'url = https://komikindo.info/series/leveling-up-by-only-eating/'

    judul: str
    judul_seo: str
    cover: str
    type_komik: str
    dewasa: bool
    statusUpdate: bool
    rilis: int
    deskripsi: str

    genre: list

    list_chapter: list[Chapter]

    r = requests.get(url, headers=headersGlobal)
    bs = BeautifulSoup(r.text, 'lxml')

    judul = bs.find(
        'div', 'series-titlex').find('h2').get_text(strip=True).lower()

    judul_seo = re.sub(r'[^a-zA-Z0-9 ]', "", judul)
    judul_seo = "-".join(judul_seo.split())

    cover = bs.find('div', 'series-thumb').find('img')['src']

    type_komik = bs.find(
        'div', 'series-infoz block').find('span').get_text(strip=True).lower()

    statusUpdate = 'Ongoing' in bs.find(
        'div', 'series-infoz block').find_all('span')[1].get_text(strip=True)

    rilis = bs.find('ul', 'series-infolist').find_all('li')
    rilis = [x for x in rilis if 'Published' in x.get_text()]
    rilis = rilis[0].find('span').get_text() if len(rilis) > 0 else 2019
    try:
        rilis = int(rilis)
    except:
        rilis = 2019

    genre = get_genre(bs)

    dewasa = 'adult' in genre

    deskripsi = bs.find('div', 'series-synops').find('p').get_text(strip=True)

    list_chapter = get_list_chapter(bs)
    list_chapter = [Chapter(href=x['href'], ke=x['ke'], image=[])
                    for x in list_chapter]

    komik = Komik(
        judul, judul_seo, cover, type_komik, dewasa, statusUpdate, rilis, deskripsi, genre
    )

    return (komik, list_chapter)


if __name__ == "__main__":
    a = detail("https://komikindo.info/series/leveling-up-by-only-eating/")
    print(a)
