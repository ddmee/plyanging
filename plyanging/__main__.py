"""Command line interface"""
# stdlib
from pathlib import Path
import random
# 3rd party
import click
# local
from plyanging.ModeListen import ModeListen
from plyanging.ReadWordList import ReadWordList


@click.command()
@click.argument('word-list')
@click.option('--learning-mode', default='listen', help='Learning mode, how you want to study')
@click.option('--sound-directory', default='.sounds', help='Where to store the language sound files')
@click.option('--phrase-order', default='random',
              type=click.Choice(('random', 'linear'), case_sensitive=False),
              help='Whether to present the phrases in random or linear order from the word list.')
def main(word_list:str, learning_mode:str, sound_directory:str, phrase_order:str):
    """Provide a word list file of language phrases to study.
    """
    word_list_path = Path(word_list)
    read_word_list = ReadWordList(word_list_path=word_list_path)
    phrases = list(read_word_list.phrases())

    if phrase_order == 'random':
        random.shuffle(phrases)
    # else ReadWordList produces linear ordered phrases by default.

    if learning_mode == 'listen':
        mode_listen = ModeListen(phrases=phrases,
                                 sound_directory=Path(sound_directory))
        mode_listen.cmdline()
    else:
        raise RuntimeError('Only "listen" mode is currently availble')


if __name__ == '__main__':
    main()