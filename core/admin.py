from django.contrib import admin

from .models import Chassis, Car

@admin.register(Chassis)
class ChassisAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
    

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'price', 'chassis']
