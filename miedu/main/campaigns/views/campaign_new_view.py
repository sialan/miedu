from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from campaigns.models import Campaign
from campaigns.forms import CampaignCreationForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def campaign(request):
    if request.method == 'POST':
        form = CampaignCreationForm(request.POST)
        if form.is_valid():
            new_campaign = form.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('campaign-list'
        else:
            return render(request, "new_blueprint.html", {"form": form})
    else:
        form = CampaignCreationForm()
        context = {"form": form}
        return render(request, "new_blueprint.html", context)
