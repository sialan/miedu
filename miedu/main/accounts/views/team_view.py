from django.shortcuts import render
from accounts.models import Account

def team(request):
    team_data_list = Account.objects.filter(is_staff=True).order_by('first_name')
    context = {'team_data_list': team_data_list}
    return render(request, 'templates/team.html', context)
