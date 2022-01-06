from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import path
from rest_framework import routers, viewsets, status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.urlpatterns import format_suffix_patterns
from . import models
from . import serializers


class TextViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all text rows to be viewed or edited.
    Text items are the raw text uploaded by a user before any translation
    occurs.
    """
    queryset = models.Text.objects.all()
    serializer_class = serializers.TextSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user,
                        creation_datetime=datetime.now())


class PhraseList(generics.ListAPIView):
    """
    API endpoint allows all phrases of a text to be viewed.

    Phrases are processed text entries spilt into phrases. Each phrase is
    associated with a Text row. Lookup phrases by text_id.

    Phrases are ordered by their primary key, though note primary keys are
    guaranteed to be continuous within a phrase set, and should not be treated
    as a simple index.
    """
    queryset = models.Phrase.objects.all().order_by('id')
    serializer_class = serializers.PhraseSerializer

    def get_queryset(self):
        """
        View should return a list of all phrases determined by the text_id
        specified in the URL
        """
        # text_id = int(self.kwargs['text_id'])
        text_id = int(self.kwargs.get('text_id', 0))
        # docs say not to use self.queryset property because it's cached once
        # and not reloaded in subsequent requests.
        # https://www.django-rest-framework.org/api-guide/generic-views/#get_querysetself
        return models.Phrase.objects.filter(text_id=int(text_id)).order_by('id')


class UserPhraseLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows all user phrase locations to be viewed or edited.
    Phrase locations are records of where a user last read to in a text, i.e.
    the last location.
    """
    queryset = models.UserPhraseLocation.objects.all()
    serializer_class = serializers.UserPhraseLocationSerializer

    def perform_create(self, serializer):
        serialised.save(user_id=self.request.user)

    def perform_update(self, serializer):
        serialised.save(user_id=self.request.user)


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'Text', TextViewSet)
router.register(r'UserPhraseLocation', UserPhraseLocationViewSet)
# Extend the router urls with the manual ones we've defined here.
# urlpatterns = format_suffix_patterns([
#     path('Phrase/<int:text_id>/', PhraseList.as_view(), name='phrase-list')
# ])
urlpatterns = [
    path('Phrase/<int:text_id>/', PhraseList.as_view(), name='phrase-list'),
]

urlpatterns += router.urls
