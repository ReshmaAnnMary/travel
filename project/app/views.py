from django.http import HttpResponse
from django.shortcuts import render
from .models import Places
from .models import Team


# Create your views here.

def demo(request):
    obj = Places.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'results': obj, 'members': obj1})
    # return HttpResponse("Welcome to inmakes project")
