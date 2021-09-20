# stdlib
from pathlib import Path
# local
from plyanging.Phrase import Phrase
from plyanging.PlaySound import PlaySound


def test_play_english_voice(tmp_path: Path) -> None:
    play_s = PlaySound(phrase=Phrase(english_text='english voice test'),
                       sound_directory=tmp_path)
    # should actually play the voice through the speakers at this point...
    eng_v_path = play_s.english_voice()
    assert eng_v_path.is_file()


def test_play_german_voice(tmp_path: Path) -> None:
    play_s = PlaySound(phrase=Phrase(german_text='Deustche-Sprachtest'),
                       sound_directory=tmp_path)
    # should actually play the voice through the speakers at this point...
    de_v_path = play_s.german_voice()
    assert de_v_path.is_file()

