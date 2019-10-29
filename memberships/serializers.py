from  memberships.models import *
from rest_framework import serializers


class membershipsAPIs(serializers.ModelSerializer):
    client = serializers.SerializerMethodField();
    service = serializers.SerializerMethodField();
    package = serializers.SerializerMethodField();
    price = serializers.SerializerMethodField();

    def get_client(self,obj):
        return Client.objects.filter(id=obj.client.id).values().first()

    def get_service(self, obj):
        return Service.objects.filter(id=obj.service.id).values().first()

    def get_package(self, obj):
        return Package.objects.filter(id=obj.package.id).values().first()

    def get_price(self, obj):
        return Price.objects.filter(id=obj.price.id).values().first()

    class Meta:
        model = Membership
        fields = '__all__'


class membershipPaymentsAPIs(serializers.ModelSerializer):
    class Meta:
        model = MembershipPayments
        fields = '__all__'