"""Command line interface"""
# stdlib
from pathlib import Path
import random
# 3rd party
import click
# local
from plyanging.ModeListen import ModeListen
from plyanging.ReadWordList import ReadWordList
from plyanging.TextFileToPhrases import TextFileToPhrases
from plyanging.Translate import translate


@click.group()
def cli():
    pass


@cli.command()
@click.argument('word-list')
@click.option('--learning-mode', default='listen',
              help='Learning mode, how you want to study')
@click.option('--sound-directory', default='.sounds',
              help='Where to store the language sound files')
@click.option('--phrase-order', default='random',
              type=click.Choice(('random', 'linear'), case_sensitive=False),
              help='Whether to present the phrases in random or linear order from'
                   ' the word list.')
@click.option('--non-stop', is_flag=True,
              help='Do not stop for user input between phrases.')
def study(word_list:str, learning_mode:str, sound_directory:str,
         phrase_order:str, non_stop:bool):
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
                                 sound_directory=Path(sound_directory),
                                 non_stop=non_stop)
        mode_listen.cmdline()
    else:
        raise RuntimeError('Only "listen" mode is currently availble')


@cli.command()
@click.argument('text_file')
@click.option('--learning-mode', default='listen',
              help='Learning mode, how you want to study')
@click.option('--sound-directory', default='.sounds',
              help='Where to store the language sound files')
@click.option('--non-stop', is_flag=True,
              help='Do not stop for user input between phrases.')
def read(text_file:str, learning_mode:str, sound_directory:str,
         non_stop:bool):
    """Read a text file contain german words, translating into english.
    """
    tftp = TextFileToPhrases(file_path=Path(text_file))
    phrases = translate(phrases=tftp.phrase_list())

    if learning_mode == 'listen':
        mode_listen = ModeListen(phrases=phrases,
                                 sound_directory=Path(sound_directory),
                                 non_stop=non_stop)
        mode_listen.cmdline()
    else:
        raise RuntimeError('Only "listen" mode is currently availble')


if __name__ == '__main__':
    cli()
