from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from campaigns.models import Campaign
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def campaign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context)
