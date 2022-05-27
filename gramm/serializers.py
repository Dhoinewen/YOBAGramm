from rest_framework import serializers
from .models import Yoba, Tags


class YobaSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Yoba
        fields = '__all__'



