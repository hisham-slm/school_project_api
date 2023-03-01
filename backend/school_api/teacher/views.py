from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return Response()


@api_view(['POST'])
def add_student(request):
    return Response()

@api_view(['GET'])
def view_student(request):
    return Response()

@api_view(['PUT'])
def change_password(request,teacher_id):
    return Response()