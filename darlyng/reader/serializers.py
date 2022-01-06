from rest_framework import serializers
from . import models


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Text
        fields = '__all__'
        read_only_fields = ('creation_datetime', 'created_by')


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phrase
        # leave out text_id because should only return phrases from a specific
        # text
        fields = ('pk', 'phrase',)
        read_only_fields = ('phrase', 'text_id')


class UserPhraseLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserPhraseLocation
        # leaving out user_id because should only return UserPhraseLocations
        # for the logged in user making the request.
        exclude = ('user_id',)
