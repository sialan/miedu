from django.shortcuts import render
from accounts.models import Account

def profile(request, account_id):
    profile_data_model = Account.objects.get(pk=account_id)
    context = {'posts': post_data_collection}
    return render(request, 'templates/blog.html', context)
