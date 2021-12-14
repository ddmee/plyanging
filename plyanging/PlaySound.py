# stdlib
from pathlib import Path
# 3rd party
from playsound import playsound
# local
from plyanging.DownloadVoice import DownloadVoice
from plyanging.Phrase import Phrase


class PlaySound:
    """Play a phrase. Will download a phrase if it's not saved locally"""
    def __init__(self, phrase: Phrase, sound_directory: Path):
        self.download_voice = DownloadVoice(phrase=phrase, directory=sound_directory)

    def english_voice(self) -> Path:
        # check if it's already on disk, if not download it
        eng_v_path = self.download_voice.english_voice_path().resolve()
        if not eng_v_path.is_file():
            self.download_voice.save_english_voice()
        playsound(str(eng_v_path))
        # suppose at this point we could return a new Phrase with
        # the location of Phrase.english_voice set to a string of the path.
        # don't need that yet...
        return eng_v_path

    def german_voice(self) -> Path:
        de_v_path = self.download_voice.german_voice_path().resolve()
        if not de_v_path.is_file():
            self.download_voice.save_german_voice()
        playsound(str(de_v_path))
        return de_v_path
