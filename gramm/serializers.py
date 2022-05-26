from rest_framework import serializers
from .models import Yoba


class YobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yoba
        fields = ('title', 'tags')