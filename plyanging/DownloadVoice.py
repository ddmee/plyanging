# stdlib
from pathlib import Path
# 3rd party
from gtts import gTTS
# local
from plyanging.Phrase import Phrase
from plyanging.secure_filename import secure_filename


class DownloadVoice:
    """Download voice translation from google translate"""

    def __init__(self, phrase: Phrase, directory: Path=None):
        """
        :optparam directory: Path, the directory to save the downloads files
            into. Defaults to the current working directory.
        """
        if directory is None:
            # not sure, but storing Path('.') in the function signature
            # might mean it's mutable, and then have weird state issues
            # across calls. So do it here instead with None.
            directory = Path('.')

        self.phrase = phrase
        self.directory = directory

    def phrase_filepath(self, phrase_text:str) -> Path:
        """Theres no guarantee the path will not clash with another phrase."""
        if len(phrase_text) <= 0:
            raise RuntimeError('phrase_text len <= 0')
        else:
            filename = secure_filename(filename=phrase_text)
            # want to control the ending to always be .mp3
            # Note this is obviously only secure if the directory is safe
            # as well. Hopefully that's guaranteed...
            return self.directory / (filename.rsplit('.', 1)[0] + '.mp3')

    def save_voice(self, phrase_text:str, lang:str) -> Path:
        """Get an mp3 of the text in spoken form, saved as an mp3 on disk"""
        filepath = self.phrase_filepath(phrase_text=phrase_text)
        tts = gTTS(phrase_text, lang=lang)
        tts.save(filepath)
        return filepath

    def english_voice_path(self) -> Path:
        return self.phrase_filepath(phrase_text=self.phrase.english_text)

    def german_voice_path(self) -> Path:
        return self.phrase_filepath(phrase_text=self.phrase.german_text)

    def save_german_voice(self) -> Path:
        return self.save_voice(phrase_text=self.phrase.german_text, lang='de')

    def save_english_voice(self) -> Path:
        return self.save_voice(phrase_text=self.phrase.english_text, lang='en')
