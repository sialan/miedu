from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render
from accounts.models import Account
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect(reverse('campaign-list'))
    else:
        # Show an error page
        return HttpResponseRedirect(reverse('registration'))
        