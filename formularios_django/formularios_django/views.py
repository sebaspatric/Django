from django.http import HttpResponse
from django.shortcuts import render
#from . import CommentForm
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm()
    return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
    #if request.method != 'GET':
    if request.method!= 'POST':
        return HttpResponse('Metodo no permitido')
    #return HttpResponse(request.GET ['name'])
    return HttpResponse(request.POST ['name'])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #Aquí irían todas las acciones a realizar cuando los datos son correctos
            return HttpResponse("Válido")
        else:
            #Aquí irían todas las acciones a realizar cuando los datos son incorrectos
            return render(request, 'widget.html', {'form': form})
