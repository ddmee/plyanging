# stdlib
from pathlib import Path
from typing import Generator
# local
from plyanging.Phrase import Phrase


class ReadWordList:
    """Read the word list."""
    def __init__(self, word_list_path:Path):
        self.word_list_path = word_list_path

    def phrases(self) -> Generator[Phrase, None, None]:
        with open(self.word_list_path, 'rt', encoding='utf-8') as word_fo:
            next_line = word_fo.readline()
            while next_line:  # reached EOF
                next_line = next_line.strip()
                if next_line != '':
                    # should be two full text lines together, first should
                    # be english, the next german. First line with text is
                    # presumed to be english. Second line is presumed to be
                    # german. If it's empty, it doesn't matter.
                    # Note, if german line is empty, rather than setting it
                    # on Phrase as '', set it as None.
                    (german_text := word_fo.readline().strip())
                    german_text = german_text if german_text else None
                    yield Phrase(english_text=next_line,
                                 german_text=german_text)
                # not matter what, move to the next line
                next_line = word_fo.readline()
