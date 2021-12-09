"""Currently uses google's exceptionally good machine translation service.

As this is a (non-profit) program to help people study a language, I hope Google
will not be deeply offended by the use of their services without paying for
api usage...

Note, need to use googletrans==3.1.0a0 due to a bug latest pypi version,
see https://github.com/ssut/py-googletrans/issues/319
"""
# stdlib
from dataclasses import replace
from typing import Generator
# 3rd party
from googletrans import Translator
# local
from plyanging.Phrase import Phrase


def translate(phrases: list[Phrase]) -> Generator[Phrase]:
    """Translates a list of phrases, returning a new copy of the phrase list"""
    translator = Translator()
    for p in phrases:
        # replace() returns a new copy of the dataclass object
        p = replace(p)
        # if we have german to translate to german...
        if p.english_text is None and p.german_text:
            p.english_text = translator.translate(p.german_text,
                                                  src='de', dest='en').text
        # if we have english to translate to german
        elif p.german_text is None and p.english_text:
            p.german_text = translator.translate(p.english_text,
                                                 src='en', dest='de').text
        # else if we already have both english and german, just skip it...
        elif p.german_text is not None and p.english_text is not None:
            # could send a debug message, but doesn't matter atm
            pass
        # else both are None, so that's bad...
        else:
            raise RuntimeError('Nothing to translate for %r' % p)
        yield p

