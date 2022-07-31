import requests
from bs4 import BeautifulSoup

headersGlobal = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/103.0.5060.114'
}


def app():
    'https://komikindo.id/komik/shuumatsu-no-valkyrie/'

    title:str
    cover:str
    type_komik:str
    dewasa:str
    list_chapter:list


    list_chapter
    

    url: str = "https://komikindo.id/komik/shuumatsu-no-valkyrie/"
    r = requests.get(url, headers=headersGlobal)
    bs = BeautifulSoup(r.text, "lxml")

    list_chapter = bs.find(id='chapter_list').find_all('li')
    list_chapter.reverse()
    list_chapter = [
        {
            'href': x.find('span', 'lchx').find('a')["href"],
            'ke' : x.find('chapter').get_text()
        }
        for x in list_chapter]

    print(list_chapter)

def halaman_read():
    'https://komikindo.id/shuumatsu-no-valkyrie-chapter-65-2/'
    url = 'https://komikindo.id/shuumatsu-no-valkyrie-chapter-65-2/'
    r = requests.get(url,headers=headersGlobal)
    bs = BeautifulSoup(r.text, "lxml")



if __name__ == '__main__':
    app()
