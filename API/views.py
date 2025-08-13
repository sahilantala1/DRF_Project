from http.client import responses

from django.core.serializers import serialize
from django.http import JsonResponse, Http404
from django.shortcuts import render,get_object_or_404
from DRF_App.models import *
from rest_framework.response import Response
from .serializers import StudentSeri,EmployeeSeri
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import mixins,generics,viewsets
from rest_framework.views import APIView
# Create your views here.
@api_view(['GET','POST'])
def j_data(req):
    if req.method == "GET":
        student_data = Students.objects.all()
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
        student = Students.objects.get(student_id=id)
    except Students.DoesNotExist:
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

class Employee(APIView):
    def get(self,request):
        employees = Employee_details.objects.all()
        serializer = EmployeeSeri(employees,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer =  EmployeeSeri(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Employee_update(APIView):
#     def get_object(self,id):
#         try:
#             return Employee_details.objects.get(id=id)
#         except Employee_details.DoesNotExist:
#             raise Http404
#
#     def get(self,request,id):
#         employee = self.get_object(id)
#         serializer = EmployeeSeri(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#
#     def delete(self,request,id):
#         employee = self.get_object(id)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self,request,id):
#         employee = self.get_object(id)
#         serializer = EmployeeSeri(employee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class Employee(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee_details.objects.all()
#     serializer_class = EmployeeSeri
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# from rest_framework import mixins, generics
#
# class EmployeeDetails(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Employee_details.objects.all()
#     serializer_class = EmployeeSeri
#     lookup_field = "id"
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class Employee(generics.ListCreateAPIView):
#     queryset = Employee_details.objects.all()
#     serializer_class = EmployeeSeri
#
# class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee_details.objects.all()
#     serializer_class = EmployeeSeri
#     lookup_field = "id"

class EmployeeViewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee_details.objects.all()
        serializer = EmployeeSeri(queryset,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = EmployeeSeri(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def retrieve(self,request,pk=None):
        employee = get_object_or_404(Employee_details,pk=pk)
        serializer = EmployeeSeri(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee_details, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self,request,pk):
        employee = get_object_or_404(Employee_details, pk=pk)
        serializer = EmployeeSeri(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)