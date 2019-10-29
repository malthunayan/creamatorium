from rest_framework import serializers
from employees.models import Employee
from users.models import User
from branches.models import Branch

class emplopyeesAPI(serializers.ModelSerializer):
    user = serializers.SerializerMethodField();

    def get_user(self,obj):
        if obj.user is not None:
            return User.objects.filter(id=obj.user.id).values().first()
        else:
            return None

    class Meta:
        model = Employee
        fields = '__all__'
