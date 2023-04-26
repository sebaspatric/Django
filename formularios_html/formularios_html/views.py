from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
    return render(request, 'form.html', {})
    #f request.method == 'GET':
    #   return render(request, 'form.html')
    #lif request.method == 'POST':
    #   return render(request, 'form.html')

def getgoal(request):
   #if request.method == 'GET':
   #    return render(request, 'success.html')
    if request.method != 'GET':
        return HttpResponse('El metodo post no esta soportado para esta ruta')
    #name = request.POST.get('name')
    name = request.GET['name']
    return render(request, 'success.html', {'name':name})

def postform(request):
    return render(request, 'postform.html', {})

def postgoal(request):
    if request.method!= 'POST':
        return HttpResponse('El metodo GET no esta soportado para esta ruta')
    info = request.POST['info']
    return render(request, 'postsuccess.html', {'info':info})





