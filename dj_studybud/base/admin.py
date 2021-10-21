from django.contrib import admin
from .models import Room, Topic, Message     #dodanie do paneli admina interfejsu do room 1/2
# Register your models here.

admin.site.register(Room)       #dodanie do paneli admina interfejsu do room 2/2
admin.site.register(Topic)       #dodanie do paneli admina interfejsu do room 2/2
admin.site.register(Message)       #dodanie do paneli admina interfejsu do room 2/2
