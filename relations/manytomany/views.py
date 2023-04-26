from django.http import HttpResponse
from django.shortcuts import render
#from . import models
from .models import Article, Publication

#primero debemos guardar los modelos para poder relacinalos con sus id 

# Create your views here.

def create(request):
    


    '''
        art1 = Article(headline='hola mundo1')
    art1.save()
    art2 = Article(headline='hola mundo2')
    art2.save()
    art3 = Article(headline='hola mundo3')
    art3.save()

    pub1 = Publication(title='publicacion1')
    pub1.save()
    pub2 = Publication(title='publicacion2')
    pub2.save()
    pub3 = Publication(title='publicacion3')
    pub3.save()
    pub4 = Publication(title='publicacion4')
    pub4.save()
    pub5 = Publication(title='publicacion5')
    pub5.save()
    pub6 = Publication(title='publicacion6')
    pub6.save()
    pub7 = Publication(title='publicacion7')
    pub7.save()

    #añadir las relaciones    
    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)

    result = art1.publications.all()

    #genera
    #publicacion1publicacion2publicacion3
    
    '''
    
    
    #consultar
    #camino spara acceder desde la publicacion donde no esta el dato
    pub1 = Publication.objects.get(id=59)
    result = pub1.article_set.all()
    

    #eliminar relaciones
    #pub1.article_set.remove(art1)



    return HttpResponse(result)