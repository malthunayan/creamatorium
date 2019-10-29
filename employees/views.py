from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from employees.serializers import emplopyeesAPI
from employees.models import Employee
# Create your views here.
class employeesData(viewsets.ModelViewSet):
    serializer_class = emplopyeesAPI

    def get_queryset(self):
        queryset = Employee.objects.all()
        gym = self.request.query_params.get('gym', None)
        if gym is not None:
            queryset = queryset.filter(gym=gym)
        return queryset


class testPost(APIView):
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = emplopyeesAPI(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data.e)
        serializer = emplopyeesAPI(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)