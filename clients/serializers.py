from  .models import *
from rest_framework import serializers


class clientsAPIs(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

