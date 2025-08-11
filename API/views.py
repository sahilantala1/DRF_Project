from django.http import JsonResponse
from django.shortcuts import render
from DRF_App.models import *
from rest_framework.response import Response
from .serializers import StudentSeri
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def j_data(req):
    if req.method == "GET":
        student_data = Student.objects.all()
        serializer = StudentSeri(student_data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif req.method == "POST":
        serializer = StudentSeri(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def StudentDetailView(req,id):
    try:
        student = Student.objects.get(student_id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if req.method == 'GET':
        serializer = StudentSeri(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif req.method == "PUT":
        serializer = StudentSeri(student, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif req.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)