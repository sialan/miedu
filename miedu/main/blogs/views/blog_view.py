from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from blogs.models import Post

def blog(request):
    post_data_collection = Post.objects.all().order_by('-created')
    paginator = Paginator(post_data_collection, 10)
    page = request.GET.get('page')

    try:
        context = {'posts': paginator.page(page)}
    except PageNotAnInteger:
       # If page is not an integer, deliver first page.
       context = {'posts': paginator.page(1)}
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        context = {'posts': paginator.page(paginator.num_pages)}

    return render(request, 'blog.html', context)
