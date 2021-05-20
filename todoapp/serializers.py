from rest_framework import serializers

from .models import todo

class todoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = todo
        fields = '__all__'