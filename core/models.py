from django.db import models

class Chassis(models.Model):
    number = models.CharField(max_length=16, help_text='Max 16 digits')
    
    class Meta:
        verbose_name = 'Chassis'
        verbose_name_plural = 'Chassis'
        
    def __str__(self) -> str:
        return self.number
    

class Automaker(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Automaker'
        verbose_name_plural = 'Automakers'

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    """
    #OneToOneField - 
        Chassis can only relate to a car and a car can relate to a chassis

    #ForeignKey (One to Many)
        Car can only relate to one automaker but an automaker can relate to several cars
    """
    chassis = models.OneToOneField(Chassis, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Automaker, on_delete=models.CASCADE)
    model = models.CharField(max_length=30, help_text='Max 30 character')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        
    def __str__(self) -> str:
        return f'{self.manufacturer} {self.chassis}'
    