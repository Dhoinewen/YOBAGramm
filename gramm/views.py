from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer

from django.shortcuts import render

from .permissions import IsAdminOrReadOnly
from .models import Yoba, Tags
from .serializers import YobaSerializer


# class YobaViewSet(viewsets.ModelViewSet):
#     queryset = Yoba.objects.all()
#     serializer_class = YobaSerializer

    # @action(methods=['get'], detail=True)
    # def tags(self, request, pk=None):
    #     tags = Tags.objects.get(pk=pk)
    #     print(tags)
    #     return Response({'tags': tags.name})


class YobaAPIList(generics.ListCreateAPIView):
    queryset = Yoba.objects.all()
    serializer_class = YobaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'gramm/test.html'
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = Yoba.objects.all()
    #     serializer = YobaSerializer(queryset, many=True)
    #     return Response(serializer.data)


class YobaAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yoba.objects.all()
    serializer_class = YobaSerializer
    permission_classes = (IsAdminOrReadOnly, )



