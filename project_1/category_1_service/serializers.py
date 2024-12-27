from rest_framework import serializers
from .models import AWB

class AWBSerializer(serializers.ModelSerializer):
    class Meta:
        model = AWB
        fields = '__all__'
