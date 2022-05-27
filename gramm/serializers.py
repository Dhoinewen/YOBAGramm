from rest_framework import serializers
from .models import Yoba, Tags


class YobaSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Yoba
        fields = '__all__'






