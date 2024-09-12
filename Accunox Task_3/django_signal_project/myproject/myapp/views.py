from django.shortcuts import render

# Create your views here.
from django.db import transaction
from django.contrib.auth.models import User

def create_user_with_atomic():
    with transaction.atomic():
        print("In atomic transaction:", transaction.get_connection().in_atomic_block)
        user = User.objects.create(username='testuser', password='password123')

