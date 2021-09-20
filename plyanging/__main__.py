"""Command line interface"""
# stdlib
from pathlib import Path
# 3rd party
import click
# local
from plyanging.ReadWordList import ReadWordList


@click.command()
@click.option('--word-list', help='Path to the word list to study.')
@click.option('--learning-mode', default='listen', help='Learning mode, how you want to study')
def main(word_list:str, mode:str):
    word_list_path = Path(word_list)
    read_word_list = ReadWordList(word_list_path=word_list_path)
    pass


if __name__ == '__main__':
    main()