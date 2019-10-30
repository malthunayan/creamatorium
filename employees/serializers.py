from rest_framework import serializers
from employees.models import Employee
from users.models import User
from branches.models import Branch

class emplopyeesAPI(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
