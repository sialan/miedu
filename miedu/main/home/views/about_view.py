from django.shortcuts import render
from articles.models import Article

def about(request):
    about_data_model = Article.objects.all().order_by('currently_featured', '-feature_score')[:4]
    context = {'about_data_model': about_data_model}
    return render(request, 'templates/about.html', context)