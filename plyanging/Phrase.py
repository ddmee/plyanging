from dataclasses import dataclass


@dataclass
class Phrase:
    english_text: str=None
    english_voice: str=None
    german_text: str=None
    german_voice: str=None

