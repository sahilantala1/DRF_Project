from rest_framework import serializers
from DRF_App.models import Students, Employee_details,Blog,Comment

class StudentSeri(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class EmployeeSeri(serializers.ModelSerializer):
    class Meta:
        model = Employee_details
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'


