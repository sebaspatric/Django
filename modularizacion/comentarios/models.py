from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    #date = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=100, default="No sign")
    #si añádo campo que no puede ser nulo a una tabla previamente creada: no se puede crear en sjango
    #opcion1 añadir un valor por defecto
    

    def __str__(self):
        return self.name
    

    
