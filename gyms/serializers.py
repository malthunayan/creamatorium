from rest_framework import serializers
from .models import *


class gymAPI(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'


