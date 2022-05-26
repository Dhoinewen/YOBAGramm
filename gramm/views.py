from rest_framework import generics
from django.shortcuts import render
from .models import Yoba
from .serializers import YobaSerializer


class YobaAPIView(generics.ListAPIView):
    queryset = Yoba.objects.all()
    serializer_class = YobaSerializer
