from django import forms
from django.core.urlresolvers import reverse
from accounts.admin import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from accounts.models import Account
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
        	return render(request, "signup.html", {"form": form})
    else:
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "signup.html", context)