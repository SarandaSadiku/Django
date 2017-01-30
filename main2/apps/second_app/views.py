from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'email': "sara@gmail.com",
        "name": "Sara"
    }
    return render(request, 'second_app/index.html',context)

def show(request, id):
    context = {
        'id':id
    }
    return render(request, 'second_app/show.html',context)
