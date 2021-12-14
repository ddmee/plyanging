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
@click.option('--start-at', type=click.INT, default=0,
               help='The phrase number to start reading from.')
@click.option('--stop-at', type=click.INT, default=None,
               help='The phrase number to stop reading at.')
@click.option('--phrase-repeat-count', type=click.INT, default=2,
               help='The number of times to repeat a phrase before continuing.')
@click.option('--translation-gap', type=click.INT, default=1,
               help='Number of seconds between reading translation and native '
                    'phrase')
@click.option('--foreign-first/--native-first', default=False,
               help='Whether to read the foreign language or native version of '
                    ' the phrase first. Defaults to reading native first.')
def read(text_file:str, learning_mode:str, sound_directory:str,
         non_stop:bool, start_at:int, stop_at:int, phrase_repeat_count:int,
         translation_gap:int, foreign_first:bool):
    """Read a text file contain german words, translating into english.
    """
    tftp = TextFileToPhrases(file_path=Path(text_file))
    # Slicing a list [0:None], returns the entire list.
    phrases = translate(phrases=tftp.phrase_list()[start_at:stop_at])

    if learning_mode == 'listen':
        mode_listen = ModeListen(phrases=phrases,
                                 sound_directory=Path(sound_directory),
                                 non_stop=non_stop,
                                 start_count=start_at,
                                 phrase_repeat_count=phrase_repeat_count,
                                 translation_gap=translation_gap,
                                 foreign_first=foreign_first)
        mode_listen.cmdline()
    else:
        raise RuntimeError('Only "listen" mode is currently availble')


if __name__ == '__main__':
    cli()
