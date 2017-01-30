from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
        #select * from courses
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    Course.objects.create(name = request.POST['name'], description= request.POST['description'])
    # insert into course(title, blog, created_at, updated_at) values(title, blog, now(), now())
    return redirect (reverse('index'))


def destroy(request, id):
    course_to_delete = Course.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'courses_app/delete_course.html',{'course': course_to_delete})
        # Othervise its a post and lets delete the course
    course_to_delete.delete()
    return redirect(reverse('index'))
