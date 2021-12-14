# stdlib
import itertools
from pathlib import Path
import time
from typing import Sequence
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
    def __init__(self, phrases: Sequence[Phrase],
                       sound_directory: Path,
                       non_stop:bool=False,
                       start_count:int=0):
        """
        :param phrases: sequence of phrases, list of phrases to run through.
        :param sound_directory: path, location to load phrase sound samples from.
        :optparam non_stop: bool, whether to wait for user input between phraeses.
        :optparam start_count: int, the index at which the first phrase passed
            to phrases starts at. Used if ModeListen is being passed only a
            slice of a large phrase list, to output the correct current phrase
            number to the user. Doesn't change behaviour of class in any way.
        """
        self.phrases = phrases
        self.sound_directory = sound_directory
        self.non_stop = non_stop
        self.start_count = start_count

    def _user_wants_next_phrase(self) -> bool:
        """Presents user with choice whether wants to repeat the current
        phrase or continue.

        Returns a boolean value. True indicates user wants the next phrase.
        False indicates they want the current phrase to be repeated.
        May also exit the program per user choice.
        """
        print('(R)epeat. (C)ontinue. (E)xit. \n'
              'Press enter after your selection. Enter = Continue\n')
        response = input()

        if 'r' == response:
            next_phrase = False
        elif 'c' == response or '' == response:
            next_phrase = True
        elif 'e' == response:  # user wants to exit the program.
            # yes e in in repeat and continue, but by this branch e
            # can only mean exit.
            exit(0)
        # else keep looking for input from the user.
        else:
            return self._user_wants_next_phrase()

        return next_phrase

    def _play_english_german(self, phrase:Phrase, count:int) -> None:
        print('-' * 20)  # mark beginning of phrase
        print('Phrase Number {0}'.format(count))
        play_sound = PlaySound(phrase=phrase, sound_directory=self.sound_directory)
        # play english sound once.
        print('English: {0}'.format(phrase.english_text))
        play_sound.english_voice()
        time.sleep(1)
        # play german sound twice.
        print('German: {0}'.format(phrase.german_text))
        play_sound.german_voice()
        time.sleep(2)
        play_sound.english_voice()
        time.sleep(1)

        play_sound.german_voice()
        print('-' * 20)  # mark end of phrase

    def _phrase_loop(self, phrase:Phrase, count:int) -> None:
        while True:
            self._play_english_german(phrase=phrase, count=count)
            if self.non_stop:
                break

            next_phrase = self._user_wants_next_phrase()
            if next_phrase:
                break
            else:
                continue

    def cmdline(self) -> None:
        """Run ModeListen in cmdline mode."""
        # specify start in enumerater() call because otherwise count says
        # it starts from 0
        for count, phrase in enumerate(self.phrases, start=self.start_count):
            self._phrase_loop(phrase=phrase, count=count)
