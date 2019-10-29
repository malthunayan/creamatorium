from rest_framework import viewsets,generics ,permissions
from .serializers import *
from gyms.models import *



class clients(viewsets.ModelViewSet):
    serializer_class = clientsAPIs

    def get_queryset(self):
        queryset = Client.objects.all()
        branch = self.request.query_params.get('branch', None)
        gym = self.request.query_params.get('gym', None)
        if gym is not None:
            queryset = queryset.filter(gym=gym)
        if branch is not None:
            queryset = queryset.filter(branch=branch)
        return queryset



# Create your views here.
