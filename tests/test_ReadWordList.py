# stdlib
from pathlib import Path
# local
from plyanging.ReadWordList import ReadWordList

def test_with_data() -> None:
    test_data = (Path(__file__) / '..' / 'test_data.txt').resolve()
    read_word_list = ReadWordList(word_list_path=test_data)
    phrase_list = list(read_word_list.phrases())
    assert len(phrase_list) == 5

    assert phrase_list[0].english_text == "These bags are heavy."
    assert phrase_list[0].german_text == "Diese Taschen sind schwer."

    assert phrase_list[1].english_text == "That's impossible."
    assert phrase_list[1].german_text == "Das ist unmöglich!"

    assert phrase_list[2].english_text == "She's watching TV."
    assert phrase_list[2].german_text == "Sie guckt Fernsehen."

    assert phrase_list[3].english_text == "This is the end."
    assert phrase_list[3].german_text is None

    assert phrase_list[4].english_text == "Who knows?"
    assert phrase_list[4].german_text == "Wer weiß."
