from dataclasses import dataclass

@dataclass
class Komik:
    judul: str
    judul_seo:str
    cover: str
    type_komik: str
    dewasa: bool
    statusUpdate: bool
    rilis: int
    deskripsi: str
    genre: list  

