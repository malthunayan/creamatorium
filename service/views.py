from django.shortcuts import render
from rest_framework import generics,viewsets
from .serilizers import *


class ServiceView(viewsets.ModelViewSet):
    serializer_class = serviceAPI
    def get_queryset(self):
        queryset = Service.objects.all()
        services = self.request.query_params.get('services',None)
        active = self.request.query_params.get('active', None)
        exclude = self.request.query_params.get('exclude', None)
        gym = self.request.query_params.get('gym', None)
        if gym is not None:
            queryset = queryset.filter(gym=gym)
        if services is not None:
            services = services.split(',')
            queryset = queryset.filter(id__in=services)
        if exclude is not None:
            exclude = exclude.split(',')
            queryset = queryset.exclude(id__in=exclude)
        if active is not None:
            queryset = queryset.filter(is_active=True)
        return queryset


# class listService(generics.ListAPIView):
#     serializer_class = serviceAPI
#
#     def get_queryset(self):
#         queryset = Service.objects.all()
#         branch = self.request.query_params.get('branch',None)
#         if branch is not None:
#             queryset = queryset.filter(branch=branch)
#         return queryset
#
# class branchService(generics.ListAPIView):
#     serializer_class = serviceAPI
#     def get_queryset(self):
#         branch = self.kwargs['branch']
#         return Service.objects.filter(branch=branch)




class PackageView(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = packagesAPI


class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = priceAPI

# Create your views here.
