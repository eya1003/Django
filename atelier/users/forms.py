from django import forms 
from .models import Person




class LoginForm(forms.ModelForm):
    class Meta:
        model = Person
        fields= ['username' , 'password']
    password=forms.CharField(label="Password", widget=forms.PasswordInput())
    #password=forms.PasswordInput()

