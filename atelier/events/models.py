
from django.db import models
from users.models import Person
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator , MinValueValidator
from datetime import date

# Create your models here.
def date_valid(val):
    if val <= date.today():
        raise ValidationError("La date doit etre superieur a la date d'aujourd'hui")
    return val



class Event(models.Model):
    title = models.CharField('TITLE',max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    CHOIX=(
        ('MUSIQUE','MUSIQUE'),
        ('CINEMA','CINEMA'),
        ('Sport','Sport')
    )
    category = models.CharField('cat', choices=CHOIX ,max_length=8)
    state = models.BooleanField(default=False)
    nbe_participant= models.IntegerField(default=0, validators=[MinValueValidator(limit_value=6)])
    evt_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organise= models.ForeignKey( Person, on_delete=models.CASCADE)
    participations = models.ManyToManyField(
        Person,
        related_name='participations',
        through='Participation'
    )

    def __str__(self):
        return f"The event title is: {self.title}"
    class Meta:
        constraints=[
                models.CheckConstraint(
                check= models.Q(
                    evt_date__gte=date.today()
                ),
                name='the event date is invalid'
            ),
        ]   

class Participation(models.Model):
    Person = models.ForeignKey(Person , on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_participation = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('Person','event')

