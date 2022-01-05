from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# django automatically adds id column an primary key per
# AppConfig.default_auto_field in reader/apps


class Text(models.Model):
    """Text is the raw text uploaded by a user before any translation occurs"""
    # text holds the raw, unprocessed uploaded text by the user
    text = models.TextField()
    # when the text was first uploaded by the user
    creation_datetime = models.DateTimeField()
    # user id that uploaded the text
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:10]


class Phrase(models.Model):
    """Processed text spilt into phrases. Each phrase is associated with
    a Text row. Phrases are naturally ordered by their primary id key."""
    phrase = models.TextField()
    text_id = models.ForeignKey(Text, on_delete=models.CASCADE)

    def __str__(self):
        return self.phrase[:10]


class UserPhraseLocation(models.Model):
    """Records the last phrase a user was reading in a text, i.e. last location
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text_id = models.ForeignKey(Text, on_delete=models.CASCADE)
    phrase_id = models.ForeignKey(Phrase, on_delete=models.CASCADE)

