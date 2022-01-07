from django.contrib import admin

from .models import Text, Phrase, UserPhraseLocation
# Register your models here.

admin.site.register([Text, Phrase, UserPhraseLocation])
