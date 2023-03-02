from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from school_admin.models import Admin

# Create your views here.
@api_view(['POST'])
def admin_login(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        # if Admin.objects.get(username = username,password = password):

        check = Admin.objects.get(username = username, password = password)
        status = True

    except:
        status = False

    return JsonResponse({'status':status})

@api_view(['POST'])
def add_teacher(request):
    return Response()


@api_view(['PUT'])
def view_teacher(request,admin_id):
    return Response()


@api_view(['GET'])
def view_student(request):
    return Response()

