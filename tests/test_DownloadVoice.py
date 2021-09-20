# stdlib
from pathlib import Path
# 3rd party
import filetype
# local
from plyanging.DownloadVoice import DownloadVoice
from plyanging.Phrase import Phrase


def _check_mp3_file(path: Path) -> None:
    # to some extent we don't care where the path is saved, just there's a
    # non-zero path present.
    assert path.is_file()
    # guess latest version of github can take a Path object, but version of
    # pypi as of sept 2021 expects a string path.
    info = filetype.guess(str(path))
    assert info.extension == 'mp3'
    assert info.mime == 'audio/mpeg'


def test_save_german_voice(tmp_path:Path) -> None:
    downv = DownloadVoice(phrase=Phrase(german_text='hallo'),
                          directory=tmp_path)
    _check_mp3_file(path=downv.save_german_voice())


def test_save_english_voice(tmp_path:Path) -> None:
    downv = DownloadVoice(phrase=Phrase(english_text='hello'),
                         directory=tmp_path)
    _check_mp3_file(path=downv.save_english_voice())
