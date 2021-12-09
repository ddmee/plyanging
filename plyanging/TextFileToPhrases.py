# stdlib
import re
from pathlib import Path
from typing import Callable
# 3rd party
import nltk.data
from nltk.tokenize import sent_tokenize
# local
from plyanging.Phrase import Phrase


# Downloading corpus for sent_tokenize is required. But download methods
# provided by nltk seem to be a bit junk. So, I've copied the required files
# to external directory. Sourced from https://www.nltk.org/nltk_data/
EXTERNAL = Path(__file__) / '..' / 'external'

# Signatures of spilt methods out to be the same as sent_tokenize.
# docs: https://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.sent_tokenize
def _split_sentence(text:str, language=None) -> list[str]:
    """Pretty naive sentence spilter.

    Currently drops any full stop at the end of a sentence.
    Should be expanded to cover ! and ?
    """
    sentences = text.split('. ')
    # get rid of any surrounding whitespace
    sentences = [s.strip() for s in sentences]
    # drop any empty sentences
    sentences = [s for s in sentences if s]
    # Note, might want to workout how to restore full stop at end of
    # sentence.
    return sentences


def _eng_re_split(text:str, language=None):
    """From https://github.com/iamarkaj/sentenceninja
    Which itself is a slight modification of https://stackoverflow.com/a/31505798/4498470
    Though, this is particular for english, it probably works OK on german.
    Could probably create a modified version of this for german
    """
    alphabets= "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = r"(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    digits = "([0-9])"
    prefixes = "(Mr|St|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|Mt|www)[.]"
    websites = "[.](com|net|org|io|gov|me|edu)"
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub(r"\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences


def sent_tokenize_wrapper(text:str, language:str):
    # Easiest thing to do is to add to the path nltk looks in, and then
    # call sent_tokenize which will calls
    # nltk.data.load(f"tokenizers/punkt/{language}.pickle")
    path = EXTERNAL.resolve()
    nltk.data.path.append(str(path))
    return sent_tokenize(text=text, language=language)


class TextFileToPhrases:
    """Convert a text file into a list of phrases."""
    # TODO only german text atm...
    # https://github.com/ssut/py-googletrans  can detect the language,
    # so could create an extra dataclass field in phrase class 'original_text',
    # then let google translate detect the original language and then fill out
    # the other phrase fields via translation.

    def __init__(self, file_path:Path, split_method:Callable=sent_tokenize_wrapper):
        """
        :optparam: split_method, a callable to split a line of text into
            sentence. Can use _split_sentence() but default is almost certainly
            better. Could use _eng_re_split().
        """
        self.file_path = file_path
        self.split_method = split_method

    def phrase_list(self) -> list[Path]:
        with open(self.file_path, 'rt') as open_file:
            line_list = open_file.readlines()

        sentence_list = []

        for line in line_list:
            sentence_list.extend(self.split_method(text=line, language='german'))

        # Now for each sentence, it's a phrase basically...
        # presuming it's german text.
        return [Phrase(german_text=s) for s in sentence_list]
