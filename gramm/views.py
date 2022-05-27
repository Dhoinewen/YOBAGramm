from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Yoba
from .serializers import YobaSerializer


class YobaViewSet(viewsets.ModelViewSet):
    queryset = Yoba.objects.all()
    serializer_class = YobaSerializer


# class YobaAPIView(APIView):
#     def get(self, request):
#         lst = Yoba.objects.all().values()
#         return Response({'yobas': list(lst)})
#
#     def post(self, request):
#         new_yoba = Yoba.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#         )
#         return Response
# class YobaAPIView(generics.ListAPIView):
#     queryset = Yoba.objects.all()
#     serializer_class = YobaSerializer
