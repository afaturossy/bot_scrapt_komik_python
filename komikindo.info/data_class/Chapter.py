from dataclasses import dataclass


@dataclass
class Chapter:
    href: str
    ke: str
    image: list

    def to_dict(self):
        return {'ke': self.ke, 'image': self.image}
