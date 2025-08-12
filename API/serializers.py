from rest_framework import serializers
from DRF_App.models import Students, Employee_details

class StudentSeri(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class EmployeeSeri(serializers.ModelSerializer):
    class Meta:
        model = Employee_details
        fields = '__all__'