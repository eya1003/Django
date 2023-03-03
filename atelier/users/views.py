from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect


# Create your views here.


def signIn(req):
    if req.method=="GET":
        form= LoginForm()
        return render(req,"users/form.html", {'form': form})
    if req.method == "POST":
        username= req.POST['username']
        pwd = req.POST['password']
        user = authenticate(req,username=username,password=pwd)
        if user is not None:
            login(req,user=user)
            return redirect('list_event_view')
        else : 
            return render(req,"users/form.html", {"error": "invalid credentials", "form":form})