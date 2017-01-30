from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login_reg/index.html')

def success(request):
    return render(request, 'login_reg/success.html')

def register(request):
    print "Here in register"
    if request.method == 'POST':
        user=User.objects.register(request.POST)

        return redirect(reverse("index"))

def login(request):
    return redirect(reverse('success'))
