from django.http import HttpResponse
from django.shortcuts import render
from .models import Reporter, Article

# Create your views here.

def create(request):
    rep = Reporter(first_name = 'Juanjo', last_name = 'Perez', email = 'efpyi@example.com')
    rep.save()

    art1 = Article(headline= 'loren ipsum dolot', pub_date = '2020-01-01', reporter = rep)
    art2 = Article(headline= 'loren ipsum dolot', pub_date = '2021-02-03', reporter = rep)
    art3 = Article(headline= 'loren ipsum dolot', pub_date = '2021-03-04', reporter = rep)
    
    art1.save()
    art2.save()
    art3.save()

    #result1 = art1.reporter.first_name
    
    #aplicar modelo de consulta
    #result2 = rep.article_set.all()
    #result3 = rep.article_set.filter(pub_date='2020-01-01')
    result4 = rep.article_set.count()

    return HttpResponse(result4)

