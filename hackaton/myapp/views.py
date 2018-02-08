from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

import requests

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    teamname = request.POST.get('teamname')
    password = request.POST.get('password')
    team_members = []

    for i in range(4):
        team_members[i] = [request.POST.get('n ame'), request.POST.get('surname'), request.POST.get('mail')]

    post_data = {
        "teamname": teamname,
        "password": password,
        "members": [
            {"name": teammate[0], "surname": teammate[1], "mail": teammate[2]} for teammate in team_members
        ]
    }

    response = requests.post('URL', post_data)

    # Zeljkec prebaci ovaj request u prikladan fajl :)

    # response = JsonResponse({'teamname':teamname,'password':password})

    return render(request, 'index.html')
