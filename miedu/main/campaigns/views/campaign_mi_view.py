from django.db.models import Q
from django.shortcuts import render
from campaigns.models import Campaign

def micampaigns(request):
    user_string = str(request.user)
    query_args = [user_string, user_string+',', ','+user_string, ','+user_string+',']
    mi_blueprint_collection = Campaign.objects.filter(account=request.user)
    supporter_blueprint_collection = Campaign.objects.filter( Q(backers__startswith=query_args[1]) | Q(backers__endswith=query_args[2]) | Q(backers__contains=query_args[3]) | Q(backers__exact=query_args[0]) | Q(backers__exact=query_args[1]))
    context = {'mi_blueprint_list': mi_blueprint_collection, 'supporter_blueprint_list': supporter_blueprint_collection}
    return render(request, 'mi_blueprint_list.html', context)
