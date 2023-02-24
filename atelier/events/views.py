from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from  django.views.generic import ListView,DetailView
from .forms import *
# Create your views here.

def homePage(request):
    return HttpResponse('<h1> welcome to Home Page</h1>')

def tesid(request,id):
    res='resultat avec id %s'
    return HttpResponse(res % id)

def renderList(req):
    list = Event[
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

def renderListEvent(req):
    # list = Event.objects.all()
    list = Event.objects.filter(state=True)
    return render(req, 'events/list.html',{'events':list})


def add_event(req):
    form= EventForm()
    if req.method == "POST" :
        form = EventForm(req.POST, req.FILES)
        if form.is_valid():
            Event.objects.create(**form.cleaned_data)
        else :
            print(form.errors)
    return render(req, "events/event_form.html",{'form':form})




#view classe based
class ListEventView(ListView):
    model = Event
    context_object_name = 'events'
    template_name='events/list.html'
    def get_queryset(self):
        return Event.objects.filter(state=True)
    
class DetailEventView(DetailView):
    model = Event
    template_name= 'events/detailsEvent.html'
    context_object_name= 'event'


    
