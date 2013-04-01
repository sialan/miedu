from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from campaigns.models import Campaign

def campaigns(request):
    blueprint_data_collection = Campaign.objects.all()
 	paginator = Paginator(blueprint_data_collection, 20)
 	page = request.GET.get('page')

 	try:
        context = {'blueprint_list': paginator.page(page)}
    except PageNotAnInteger:
    	# If page is not an integer, deliver first page.
    	context = {'blueprint_list': paginator.page(1)}
    except EmptyPage:
    	# If page is out of range (e.g. 9999), deliver last page of results.
        context = {'blueprint_list': paginator.page(paginator.num_pages)}
        
    return render(request, 'blueprints.html', context)
