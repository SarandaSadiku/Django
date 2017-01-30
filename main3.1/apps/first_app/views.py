from django.shortcuts import render
from .models import People
# Create your views here.
def index(request):
    People.objects.create(first_name = 'Sara', last_name = 'Sadiku')
    people = People.objects.all()
    print (people)
    return render(request, 'first_app/index.html')
