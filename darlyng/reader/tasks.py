from .models import Text, Phrase
from plyanging.TextFileToPhrases import text_to_phrase


def new_phrases(text_id: int):
    # get the text
    text = Text.objects.get(pk=text_id)
    # hardcoded as german input atm...
    phrases = text_to_phrase(text=text.text, language='german')
    for phrase in phrases:
        # in django's ORM, specifying a foreign key, you specify the entire
        # instance rather than the pk int.
        Phrase(phrase=phrase, text_id=text).save()


def update_phrases(text_id: int):
    # first delete the old phrases
    text = Text.objects.get(pk=text_id)
    Phrase.objects.filter(text_id=text).delete()
    # deleting the old phrases ought to trigger the delete on cascade feature
    # of the User Phrase Location, thus wiping the user phrase location as
    # well, which is good, because existing saved phrase location has no
    # guarantee to be relevant to the new phrase list.
    new_phrases(text_id=text_id)
