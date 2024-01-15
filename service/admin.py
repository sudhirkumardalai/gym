from django.contrib import admin
from service.models import *

# Register your models here.
class Admin(admin.ModelAdmin):
    display=('name','contact','gender','address')


admin.site.register(gym,Admin)