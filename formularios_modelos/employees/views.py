from django.http import HttpResponse
from django.shortcuts import render

from .forms import EmployeeForm
# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.") 
    form = EmployeeForm()
    return render(request, 'index.html', {'form': form})
