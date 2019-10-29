from django.shortcuts import render
from rest_framework import viewsets
from branches.models import Branch
from branches.serializers import branchAPI

# Create your views here.
class branchData(viewsets.ModelViewSet):
    serializer_class = branchAPI

    def get_queryset(self):
        queryset = Branch.objects.all()
        gym = self.request.query_params.get('gym',None)
        active = self.request.query_params.get('active',None)
        if gym is not None:
            queryset = queryset.filter(gym=gym)
        if active is not None:
            queryset = queryset.filter(is_active=True)
        return queryset
