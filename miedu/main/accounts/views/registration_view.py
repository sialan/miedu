from django import forms
from accounts.admin import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from accounts.models import Account


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserCreationForm()
        return render_to_response("signup.html", {
            'form': form,
        })