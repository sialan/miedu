from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect(reverse('home'))