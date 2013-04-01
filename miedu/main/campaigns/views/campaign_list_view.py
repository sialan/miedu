from django.shortcuts import render
from campaigns.models import Campaign

def campaigns(request, account_id):
    blueprint_data_collection = Account.objects.all()
    context = {'blueprint_list': blueprint_data_collection}
    return render(request, 'blueprints.html', context)
