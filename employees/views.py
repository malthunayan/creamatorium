from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserAPI
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

    def create(self, request,*args,**kwargs):
        emplopyeePostData = request.data['employee']
        if "email" not in emplopyeePostData or emplopyeePostData['email'] is None or emplopyeePostData['email'] == "":
            emplopyeePostData['email'] = (
                        emplopyeePostData['first_name'] + "." + emplopyeePostData['last_name'] + "@gym.com").replace(
                " ", "");
            print(emplopyeePostData['email'])
        EmployeeSerializer = emplopyeesAPI(data=emplopyeePostData)
        if EmployeeSerializer.is_valid():
            EmployeeSerializer.save()
            if request.data['createUser']:
                userData = {}
                userData['email'] = EmployeeSerializer.data['email']
                userData['first_name'] = EmployeeSerializer.data['first_name']
                userData['last_name'] = EmployeeSerializer.data['last_name']
                userData['mobile'] = EmployeeSerializer.data['mobile']
                userData['password'] = EmployeeSerializer.data['mobile']
                userData['username'] = EmployeeSerializer.data['first_name'] + str(EmployeeSerializer.data['id'])
                UserSerializer = UserAPI(data=userData)
                if UserSerializer.is_valid():
                    UserSerializer.save()
                    return Response({"username": UserSerializer['username'], "password": UserSerializer['password']},
                        status=status.HTTP_201_CREATED)
            return Response(EmployeeSerializer.data, status=status.HTTP_201_CREATED)
        return Response(EmployeeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class testPost(APIView):
#     def get(self, request, format=None):
#         employees = Employee.objects.all()
#         serializer = emplopyeesAPI(employees, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = emplopyeesAPI(data=request.data['e'])
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)