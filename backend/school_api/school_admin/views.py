from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    pass

@api_view(['POST'])
def add_teacher(request):
    return Response()


@api_view(['PUT'])
def view_teacher(request,admin_id):
    return Response()


@api_view(['GET'])
def view_student(request):
    return Response()

