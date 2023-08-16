from django.db import models

class Chassis(models.Model):
    number = models.CharField(max_length=16, help_text='Max 16 digits')
    
    class Meta:
        verbose_name = 'Chassis'
        verbose_name_plural = 'Chassis'
        
    def __str__(self) -> str:
        return self.number


class Car(models.Model):
    chassis = models.OneToOneField(Chassis, on_delete=models.CASCADE)
    model = models.CharField(max_length=30, help_text='Max 30 character')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        
    def __str__(self) -> str:
        return self.model
    