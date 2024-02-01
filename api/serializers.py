from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Todo
        fields  = ["id","name", "description","done"]


class EditSerializer(serializers.Serializer):
    name          = serializers.CharField()
    description   = serializers.CharField()
    done          = serializers.BooleanField()