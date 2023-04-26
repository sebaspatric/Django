from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

# Create your views here.

def update(request):
    author = Author.objects.get(id=1)
    author.name = 'Ladams'
    author.email = 'ladams@example.com'
    author.save()
    return HttpResponse("Modificado")

def queries(request):
    #obtener todos los elementos
    authors = Author.objects.all()
    
    #trae la informacion
    #return render(request, 'post/queries.html', {'authors': authors})

    #return HttpResponse("You're at the queries page.")
    #return render(request, 'post/queries.html', {})
    #return HttpResponse("You're at the queries page.")

    #--------------------------------------------------
    #filtro obtener datos filtrados por condicion... se obtiene una coleccion de objetos
    filtered = Author.objects.filter(email='ladams@example.com')

    #return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered})
    #----------------------------------------------
    #obtener un único objeto (filtrado)
    author = Author.objects.get(id=1)

    #limits = Author.objects.all().order_by('-id')[0:10]
    limits = Author.objects.all()[0:10]

    #Obtener 10 valores saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    #order by
    orders = Author.objects.all().order_by('email')

    #filtro de comparacion
    #busqueda por id que sea menor o ig ual a 15
    filtered2 = Author.objects.filter(id__lte=15) #lte lower than equals 

    #Obtener todos los autores que contienen en su nombre la palabra yes
    filtered3 = Author.objects.filter(name__contains='TV')

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders, 'filtered2': filtered2, 'filtered3': filtered3}) 
    #----------------------------------------------
    #obtener un único objeto (filtrado)

