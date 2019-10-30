from rest_framework import viewsets,generics ,permissions
from .serializers import UserAPI
from users.models import User
from rest_framework.permissions import IsAuthenticated


class UserData(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserAPI

# Create your views here.
