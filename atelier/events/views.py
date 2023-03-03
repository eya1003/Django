from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Event
from  django.views.generic import ListView,DetailView, CreateView, UpdateView
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

#ajout d'un evenement
def add_event(req):
    form= EventForm()
    if req.method == "POST" :
        form = EventForm(req.POST, req.FILES)
        if form.is_valid():
            Event.objects.create(**form.cleaned_data)
            return redirect('list_event_view')
        else :
            print(form.errors)
    return render(req, "events/event_form.html",{'form':form})

@login_required(login_url="/users/login") # doit etre l'url
def create_event(req):
    if req.method == "GET": 
        form= EventModelForm()
        return render(req, "events/event_form.html",{'form':form})
    if req.method == "POST":
        form = EventModelForm(req.POST, req.FILES)
        if form.is_valid():
            Event = form.save(commit=False) #false car avant d'enregistrer je veux modifier qq chose dans l'instance,
            Event.save() #devient save(commit=true)
            return redirect('list_event_view')
        else: 
            return render(req, "events/event_form.html",{'form':form})
        


#view classe based
class ListEventView(LoginRequiredMixin,ListView):
    login_url="login" #nom du path
    model = Event
    context_object_name = 'events'
    template_name='events/list.html'
    def get_queryset(self):
        return Event.objects.filter(state=True)
    
class DetailEventView(LoginRequiredMixin,DetailView):
    login_url="login" #nom du path
    model = Event
    template_name= 'events/detailsEvent.html'
    context_object_name= 'event'

class CreateEvent(LoginRequiredMixin,CreateView):
    login_url="login" #nom du path
    model=Event
    template_name= "events/event_form.html"
    form_class= EventModelForm
    success_url= reverse_lazy('list_event_view')


class UpdateEvent(LoginRequiredMixin,UpdateView):
    login_url="login" #nom du path
    model=Event
    template_name= "events/event_form.html"
    form_class= EventModelForm
    success_url= reverse_lazy('list_event_view')
    
