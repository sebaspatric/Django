from datetime import date
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    #last_name = models.CharField(max_length=100)
    #models.EmailField(_(""), max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

class Entry(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #si el autor es eliminado eliminamos las entradas relacionadas
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today)#auto_now_add=True)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline