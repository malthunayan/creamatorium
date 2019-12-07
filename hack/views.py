from django.shortcuts import render
from hack.models import Order
from rest_framework import viewsets
from hack.serializers import OrderSeri

# Create your views here.


class orderView(viewsets.ModelViewSet):
    serializer_class = OrderSeri
    def get_queryset(self):
        queryset = Order.objects.all()

        status = self.request.query_params.get('status', None)

        if status is not None:
            status = status.split(',')
            queryset = queryset.filter(status__in=status)
        return queryset

