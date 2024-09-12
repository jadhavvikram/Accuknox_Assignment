from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_user_view(request):
    user = User.objects.create(username='testuser', password='password123')
    return HttpResponse('User created!')

