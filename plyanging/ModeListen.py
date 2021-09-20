# stdlib
from pathlib import Path
import time
from typing import Generator
# 3rd party
# local
from plyanging.Phrase import Phrase
from plyanging.PlaySound import PlaySound


class ModeListen:
    """Iterate through a bunch of Phrase, listen mode only.

    Listen mode:
        write to terminal english_text
        play sound for english_voice one.
        sleep 2 seconds
        then,
        write to terminal german_text
        play sound for german_voice twice. Delay 2 seconds between plays.
        sleep 2 seconds.
    """
    def __init__(self, phrases: Generator[Phrase, None, None],
                       sound_directory: Path):
        """
        :param phrases: generator, list of phrases to run through.
        :param sound_directory: path, location to load phrase sound samples from.
        """
        self.phrases = phrases
        self.sound_directory = sound_directory

    def cmdline(self):
        """Run ModeListen in cmdline mode."""
        for phrase in self.phrases():
            play_sound = PlaySound(phrase=phrase, sound_directory=self.sound_directory)
            # play english sound once.
            print('English: {0}'.format(phrase.english_text))
            play_sound.english_voice()
            time.sleep(2)
            # play german sound twice.
            print('German: {0}'.format(phrase.german_text))
            play_sound.german_voice()
            time.sleep(2)
            play_sound.german_voice()
            # prepare for next phrase
            print('-'*20)
            time.sleep(2)
