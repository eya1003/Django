from django import forms
from users.models import Person
from .models import Event
CHOIX=(
    ('MUSIQUE','MUSIQUE'),
    ('CINEMA','CINEMA'),
    ('Sport','Sport')
)
class EventForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="description", widget=forms.Textarea(attrs={
        'class' :'form-control'
    }))
    image = forms.ImageField(label="Event image")
    category= forms.ChoiceField(label="category event", choices=CHOIX, widget=forms.RadioSelect())
    nbe_participant= forms.IntegerField(min_value=0)
    evt_date = forms.DateField(
        label= "Event date",
        widget= forms.DateInput(attrs={
            'type' : 'date',
            'class' : 'form-control date-input'
        })
    )
    #organise= forms.ModelChoiceField(label="Organizer",queryset=Person.objects.all())

#modelForm car elle va hérité de notre classe precedante
#form on a pas generer les validators hors que modelForm on doit le faire 
class EventModelForm(forms.ModelForm): 
    class Meta:
        model= Event
        #fields='__all__'
        fields= ['title','description' , 'image' , 'category' , 'nbe_participant' , 'evt_date' , 'organise']
        #exclude=('state',) pour ne pas recuperer l'attribut
    evt_date = forms.DateField(
        label= "Event date",
        widget= forms.DateInput(attrs={
            'type' : 'date',
            'class' : 'form-control date-input'
        })
    )
    organise= forms.ModelChoiceField(label="Organizer",queryset=Person.objects.all())
