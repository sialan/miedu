from django.shortcuts import render
from blogs.models import Post

def blog(request):
    post_data_collection = Post.objects.all().order_by('-created')
    context = {'posts': post_data_collection}
    return render(request, 'blog.html', context)
