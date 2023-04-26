from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment

# Create your views here.   

def test(request):
    return HttpResponse("Hello, world. You're at the test page.")

def create(request):
    #crea el objeto desde su constructor
    #comment = Comment(name = "Juanjo", score=5, comment="This is a comment")
    #comment.save()
    comment = Comment.objects.create(name = "Alex", score=6, comment="This is a comment2")
    
    return HttpResponse("You're at the create page.")

def delete(request):
    #comment = Comment.objects.get(id=1)
    #comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse("You're at the delete #page.")

''' 
def delete(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return HttpResponse("Hello, world. You're at the delete #page.")
'''

