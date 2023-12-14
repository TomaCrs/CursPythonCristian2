from django.shortcuts import render
from rest_framework import viewsets

from ap1.models import Reteta
from my_api.serializers import RetetaSerializers


# Create your views here.
class RetetaViewSet(viewsets.ModelViewSet):
    queryset = Reteta.objects.all()
    serializer_class = RetetaSerializers