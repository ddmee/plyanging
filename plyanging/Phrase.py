# stdlib
from dataclasses import dataclass
from reprlib import repr as arepr


@dataclass
class Phrase:
    english_text: str=None
    english_voice: str=None
    german_text: str=None
    german_voice: str=None

    def __repr__(self):
        return (f'Phrase(english_text={arepr(self.english_text)}, '
                f'german_text={arepr(self.german_text)})')

