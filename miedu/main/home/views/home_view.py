from django.shortcuts import render
from campaigns.models import Campaign

def index(request):
    featured_campaign_list = Campaign.objects.all().order_by('currently_featured', '-feature_score')[:4]
    context = {'featured_campaign_list': featured_campaign_list}
    return render(request, 'templates/index.html', context)