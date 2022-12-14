from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from applications.spam.models import Spam
from applications.spam.serializers import SpamSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class SpamAPIView(ModelViewSet):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
