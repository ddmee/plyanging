from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers, viewsets
from . import models
from . import serializers

# Create your views here.
# def index(request):
#     return HttpResponse('Reader')


class TextViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all text to be viewed or edited
    """
    queryset = models.Text.objects.all()
    serializer_class = serializers.TextSerializer


class PhraseViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows all phrases to be viewed
    """
    queryset = models.Phrase.objects.all()
    serializer_class = serializers.PhraseSerializer


class UserPhraseLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all user phrase locations to be viewed or edited
    """
    queryset = models.UserPhraseLocation.objects.all()
    serializer_class = serializers.UserPhraseLocationSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Text', TextViewSet)
router.register(r'Phrase', PhraseViewSet)
router.register(r'UserPhraseLocation', UserPhraseLocationViewSet)
