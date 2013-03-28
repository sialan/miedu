from django.shortcuts import render
from accounts.models import Account

def registration(request):
    team_data_model = Article.objects.all(is_staff=True).order_by('first_name')
    context = {'about_data_list': about_data_list}
    return render(request, 'templates/team.html', context)
