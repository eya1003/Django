from django.contrib import admin
from .models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
        list_display = ['cin','email','username','is_active','is_superuser']
        list_filter = ['cin' , 'email']
        list_per_page = 5
        ordering = ['-cin']
        search_fields = ('cin','email')
        readonly_fields = ['last_login' , 'date_joined']

        fieldsets=[
            ['Credentials',{
                'classes':['collapse'],
                'fields':['first_name', 'last_name', 'cin' , 'username' ,'password', 'is_superuser' , 'is_staff' , 'is_active' , 'groups']
                } 
            ],
            ['Date',{
                'fields':['last_login' , 'date_joined']
            }]
        ]
admin.site.register(Person,PersonAdmin)