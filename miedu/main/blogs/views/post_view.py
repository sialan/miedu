from django.shortcuts import render
from blogs.models import Post

def post(request, post_id):
    post_data_model = Post.objects.get(id=post_id)
    context = {'post': post_data_model}
    return render(request, 'templates/post.html', context)
