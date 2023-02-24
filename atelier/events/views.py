from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def homePage(request):
    return HttpResponse('<h1> welcome to Home Page</h1>')

def tesid(request,id):
    res='resultat avec id %s'
    return HttpResponse(res % id)

def renderList(req):
    list = [
    {
    'title': 'Event 1',
    'description': 'description 1',
    },
    {
    'title': 'Event 2',
    'description': 'description 2',
    },
    {
    'title': 'Event 3',
    'description': 'description 3',
    }
    ]
    return render(req, 'events/listStatic.html',{'events':list})
