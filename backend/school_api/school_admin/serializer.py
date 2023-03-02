from rest_framework import serializers
from .models import Admin


class AdminSerializer(serializers.Serializer):
    class Meta:
        model = Admin
        fields = '__all__'