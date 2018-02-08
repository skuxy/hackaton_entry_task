import requests

from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        teamname = request.POST.get('Teamname')
        password = request.POST.get('Password')

        team_member = [{} for _ in range(4)]
        team_member[0] = {
            'name':     request.POST.get('Name1'),
            'surname':  request.POST.get('Surname1'),
            'mail':     request.POST.get('email1')
            }
        team_member[1] = {
            'name':     request.POST.get('Name2'),
            'surname':  request.POST.get('Surname2'),
            'mail':     request.POST.get('email2')
            }
        team_member[2] = {
            'name':     request.POST.get('Name3'),
            'surname':  request.POST.get('Surname3'),
            'mail':     request.POST.get('email3')
            }

        team_member[3] = {
            'name':     request.POST.get('Name4'),
            'surname':  request.POST.get('Surname4'),
            'mail':     request.POST.get('email4')
        }

        post_data = {
            "Teamname": teamname,
            "Password": password,
            "Members": [
                {
                    "name":     team_member[0]['name'],
                    "surname":  team_member[0]['surname'],
                    "mail":     team_member[0]['mail'],
                },
                {
                    "name":     team_member[1]['name'],
                    "surname":  team_member[1]['surname'],
                    "mail":     team_member[1]['mail'],
                },
                {
                    "name":     team_member[2]['name'],
                    "surname":  team_member[2]['surname'],
                    "mail":     team_member[2]['mail'],
                },
                {
                    "name":     team_member[3]['name'],
                    "surname":  team_member[3]['surname'],
                    "mail":     team_member[3]['mail'],
                },
            ],
        }

        response = requests.post("http://52.233.158.172/change/api/en/account/register", post_data)

    return HttpResponse(response.json, content_type='application/json')
