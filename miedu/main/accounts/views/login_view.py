from django.shortcuts import render
from accounts.models import Account

def login(request):
    post_data_collection = Post.objects.all().order_by('-created')
    context = {'posts': post_data_collection}
    return render(request, 'templates/blog.html', context)
