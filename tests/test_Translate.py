# stdlib
# 3rd party
import pytest
# local
from plyanging.Phrase import Phrase
from plyanging.Translate import translate


def test_translate_handles_german_english():
    """This test might be flaky given translation engine might return
    different translations. However... let's hope the examples are so
    straight forward they are basically stable.
    """
    phrases = [
        Phrase(english_text='my name is john.'),
        Phrase(german_text='Woher kommst du?'),
        # purposefully the german is not the translation of the english
        # to check the translator function skipped this as both language
        # phrases where already filled out...
        Phrase(english_text='It is cold.', german_text='warum nicht.'),
    ]
    result = translate(phrases=phrases)

    assert result[0].english_text == 'my name is john.'
    assert result[0].german_text == 'mein Name ist John.'
    assert result[0].english_voice is None
    assert result[0].german_voice is None

    assert result[1].german_text == 'Woher kommst du?'
    assert result[1].english_text == 'Where do you come from?'
    assert result[1].english_voice is None
    assert result[1].german_voice is None

    assert result[2].english_text == 'It is cold.'
    assert result[2].german_text == 'warum nicht.'
    assert result[2].english_voice is None
    assert result[2].german_voice is None


def test_translate_will_raise_error_on_empty_phrase():
    with pytest.raises(RuntimeError):
        # empty phrase means we cannot translate anything, and that's probably
        # a bug somewhere, so translate() is meant to throw an error here.
        translate(phrases=[Phrase()])
