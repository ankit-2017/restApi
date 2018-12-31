from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeesSerializers

class employeesList(APIView):
    def get(self, request):
        employee = Employees.objects.all();
        serializer = EmployeesSerializers(employee, many = True)
        return Response(serializer.data)




# Create your views here.
