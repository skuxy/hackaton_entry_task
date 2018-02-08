import requests

from django.http import HttpResponse
from django.shortcuts import render
import json

BASE_LOGIN_URL = "http://52.233.158.172/change/api/hr/account/"
BASE_INFO_URL = "http://52.233.158.172/change/api/hr/team/details/"


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        teamname = request.POST.get('teamname')
        password = request.POST.get('password')

        team_member = [{} for _ in range(4)]
        team_member[0] = {
            'name':     request.POST.get('name1'),
            'surname':  request.POST.get('surname1'),
            'mail':     request.POST.get('email1')
        }

        team_member[1] = {
            'name':     request.POST.get('name2'),
            'surname':  request.POST.get('surname2'),
            'mail':     request.POST.get('email2')
        }

        team_member[2] = {
            'name':     request.POST.get('name3'),
            'surname':  request.POST.get('surname3'),
            'mail':     request.POST.get('email3')
        }

        team_member[3] = {
            'name':     request.POST.get('name4'),
            'surname':  request.POST.get('surname4'),
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

        response = requests.post(
            BASE_LOGIN_URL + "register",
            json.loads(json.dumps(post_data))
        )

        print(response.json())

    return HttpResponse(response.json, content_type='application/json')


def login(request):
    teamname = request.POST.get('teamname')
    password = request.POST.get('password')

    post_data = {
        "Teamname": teamname,
        "Password": password,
    }

    response = requests.post(
        BASE_LOGIN_URL + "login",
        json.loads(json.dumps(post_data))
    )

    response_json = json.loads(response.json()["Result"])
    team_id = response_json["TeamId"]
    team_name = response_json["TeamName"]
    auth_token = response_json["AuthorizationToken"]

    return show_details(request, team_id=team_id, team_name=team_name, auth_token=auth_token)


def show_details(request, team_id, team_name, auth_token):
    response = requests.get(BASE_INFO_URL + str(team_id), headers={'X-Authorization': str(auth_token)})
    return HttpResponse()
