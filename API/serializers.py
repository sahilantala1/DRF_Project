from rest_framework import serializers
from DRF_App.models import Student

class StudentSeri(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'