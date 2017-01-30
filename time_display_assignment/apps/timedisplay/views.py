from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    i = datetime.datetime.now()
    currentDate = ("%s/%s/%s" % (i.day,i.month,i.year))
    currentTime =  (" %s:%s:%s" % (i.hour,i.month,i.second))

    context={
    "currentDate":currentDate,
    "currentTime":currentTime
    }
    return render(request, 'timedisplay/index.html', context)
