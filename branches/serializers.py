from rest_framework import serializers
from branches.models import Branch


class branchAPI(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
