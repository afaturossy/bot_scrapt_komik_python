from httpx import main
import requests
from baca_gambar import baca_gambar, baca_gambar_session
from detail_komik import detail
from data_class.Chapter import Chapter
from halaman_root import halaman_root
from threading import Thread
import asyncio

NEXT_PUBLIC_BACKEND_DATABASE = 'http://igabut.com:50302'


def uploadKomik(data_json: dict):
    url = f'{NEXT_PUBLIC_BACKEND_DATABASE}/add'
    r = requests.post(url, json=data_json)
    print(r.status_code)


def uploadKomikPart(data_json: dict):
    max_length_chapter = 20
    index_batas = 0
    chapter = data_json["chapter"]
    # membagi list
    chapter_new = ""

    url = f'{NEXT_PUBLIC_BACKEND_DATABASE}/add'
    r = requests.post(url, json=data_json)
    print(r.status_code)


def cekChapterAkhirDiDatabase(judul, list_chapter_ke):
    url = f'{NEXT_PUBLIC_BACKEND_DATABASE}/add/cek-chapter-terakhir/{judul}'
    try:
        r = requests.get(url)
        if r.status_code == 200 and r.text != 'komik kosong':
            batas_index = 0
            ch_terakhit = r.text
            for index, value in enumerate(list_chapter_ke):
                if value == ch_terakhit:
                    batas_index = index

            return batas_index
        elif r.status_code == 200 and r.text == 'komik kosong':
            return 0
        else:
            return None
    except:
        return None


def all(url):

    try:
        data = detail(url)
    except:
        return

    komik, chapter = data

    list_chapter_ke = [x.ke for x in chapter]

    last_chapter_index = cekChapterAkhirDiDatabase(
        komik.judul_seo, list_chapter_ke)

    if last_chapter_index == None:
        print(f'{url} -> gagal, respon last_chapter_index None')
        return

    chapter_belum_diupload = [x for index, x in enumerate(
        chapter) if index > last_chapter_index]

    print(f'index akhir {last_chapter_index}')
    print(f'jumlah chapter akan di upload {len(chapter_belum_diupload)}')

    if len(chapter_belum_diupload) <= 0:
        return

    list_image = [x.href for index, x in enumerate(chapter_belum_diupload)]

    list_image = baca_gambar_session(list_image)

    new_chapter = [Chapter(x.href, x.ke, image=list_image[index])
                   for index, x in enumerate(chapter_belum_diupload)]

    chapter_dict = [x.to_dict() for x in new_chapter]
    test = {
        'code': 'Abangjav123789',
        'judul': komik.judul,
        'judulSeo': komik.judul_seo,
        'cover': komik.cover,
        'type': komik.type_komik,
        'statusUpdate': komik.statusUpdate,
        'deskripsi': komik.deskripsi,
        'dewasa': komik.dewasa,
        'rilis': komik.rilis,
        'genre': komik.genre,
        'chapter': chapter_dict
    }

    # print(test)
    uploadKomik(test)


async def all_async(url):

    try:
        data = detail(url)
    except:
        return

    komik, chapter = data

    list_chapter_ke = [x.ke for x in chapter]

    last_chapter_index = cekChapterAkhirDiDatabase(
        komik.judul_seo, list_chapter_ke)

    if last_chapter_index == None:
        print(f'{url} -> gagal, respon last_chapter_index None')
        return

    chapter_belum_diupload = [x for index, x in enumerate(
        chapter) if index > last_chapter_index]

    # print(f'index akhir {last_chapter_index}')
    print(f'jumlah chapter akan di upload {len(chapter_belum_diupload)}')

    if len(chapter_belum_diupload) <= 0:
        return

    list_image = [x.href for index, x in enumerate(chapter_belum_diupload)]

    list_image = baca_gambar_session(list_image)

    new_chapter = [Chapter(x.href, x.ke, image=list_image[index])
                   for index, x in enumerate(chapter_belum_diupload)]

    chapter_dict = [x.to_dict() for x in new_chapter]
    test = {
        'code': 'Abangjav123789',
        'judul': komik.judul,
        'judulSeo': komik.judul_seo,
        'cover': komik.cover,
        'type': komik.type_komik,
        'statusUpdate': komik.statusUpdate,
        'deskripsi': komik.deskripsi,
        'dewasa': komik.dewasa,
        'rilis': komik.rilis,
        'genre': komik.genre,
        'chapter': chapter_dict
    }

    # print(test)
    uploadKomik(test)


async def main_async():
    jumlah_halaman = 35

    for page in range(jumlah_halaman, 0, -1):

        daftar_komik = halaman_root(page)
        task = []

        for komik in daftar_komik:

            print(f'{komik} - halaman {page}/{jumlah_halaman}')

            task.append(all_async(komik))

            # all(komik)

        await asyncio.gather(*task)


if __name__ == "__main__":
    asyncio.run(main_async())

    # jumlah_halaman = 35

    # for page in range(jumlah_halaman, 30, -1):

    #     daftar_komik = halaman_root(page)
    #     for komik in daftar_komik:
    #         print(f'{komik} - halaman {page}/{jumlah_halaman}')

    #         all(komik)
    #         break
    #     break
