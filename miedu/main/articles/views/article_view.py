from django.shortcuts import render
from articles.models import Article

def article(request, article_id):
    article_data_model = Article.objects.get(id=article_id)
    context = {'article': article_data_model}
    return render(request, 'article.html', context)
