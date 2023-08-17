from django.contrib import admin

from .models import Chassis, Car, Automaker

@admin.register(Automaker)
class Automaker(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Chassis)
class ChassisAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
    

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model','price', 'chassis', 'get_drivers']
    
    # To show Many to Many fields on admin page
    def get_drivers(self, obj):
        return ', '.join([d.username for d in obj.driver.all()])
    
    get_drivers.short_description = 'Drivers'
