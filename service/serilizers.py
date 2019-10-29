from rest_framework import serializers
from .models import *
# from django.core import serializers as sjon

class serviceAPI(serializers.ModelSerializer):
    package = serializers.SerializerMethodField()
    def get_package(self,obj):
        query = Package.objects.filter(service=obj)
        s = packagesAPI(query,many=True)
        return s.data
    class Meta:
        model = Service
        fields = '__all__'

class priceAPI(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class packagesAPI(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    def get_price(self,obj):
        query = Price.objects.filter(package=obj)
        s = priceAPI(query,many=True)
        return s.data
        # return list(Price.objects.all().values())
        # return sjon.serialize("json", Price.objects.filter(package=obj))
    class Meta:
        model = Package
        fields = '__all__'



