from django.shortcuts import render
from campaigns.models import Campaign

def blueprint(request, campaign_id):
    campaign_data_model = Campaign.objects.get(id=campaign_id)
    context = {'campaign': campaign_data_model}
    return render(request, 'blueprint.html', context)
