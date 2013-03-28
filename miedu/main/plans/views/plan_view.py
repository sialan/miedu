from django.shortcuts import render
from articles.models import Article

def plan(request):
    article_data_list = Article.objects.all(main=False).order_by('title')
    context = {'article_data_list': article_data_list}
    
    return render(request, 'templates/learn.html', context)
