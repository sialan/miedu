from django.shortcuts import render
from campaigns.models import Campaign

def campaigns(request):
    blueprint_data_collection = Campaign.objects.all()
    context = {'blueprint_list': blueprint_data_collection}
    return render(request, 'blueprints.html', context)
