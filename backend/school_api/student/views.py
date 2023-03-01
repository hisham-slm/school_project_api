from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def home(request):
    return Response()

@api_view(['GET'])
def profile(request,stud_id):
    return Response()

@api_view(['PUT'])
def change_password(request,stud_id):
    return Response()