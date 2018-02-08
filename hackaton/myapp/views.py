import requests

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import json

BASE_LOGIN_URL = "http://52.233.158.172/change/api/en/account/"
BASE_INFO_URL = "http://52.233.158.172/change/api/en/team/details/"
BASE_CONFIRM_URL = "http://52.233.158.172/change/api/en/team/confirm"
GITHUB_REPO_URL = "https://github.com/skuxy/hackaton_entry_task"


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
            json.dumps(post_data),
            headers={
                'Content-Type': 'application/json'
            }
        )

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
        json.dumps(post_data),
        headers={
                'Content-Type': 'application/json'
        }
    )

    response_json = json.loads(response.json()["Result"])
    team_id = response_json["TeamId"]
    team_name = response_json["TeamName"]
    auth_token = response_json["AuthorizationToken"]

    if response.status_code == 200:
        print('go to show details')
        requests.post(
            BASE_CONFIRM_URL,
            headers={'X-Authorization': str(auth_token)},
            params={
                "id": team_id,
                "repository": GITHUB_REPO_URL
            }
        )
        return show_details(request, team_id=team_id, team_name=team_name, auth_token=auth_token)
    else:
        print('show details didnt happen')
        return redirect('/')


def show_details(request, team_id, team_name, auth_token):
    response = requests.get(
        BASE_INFO_URL + str(team_id),
        headers={'X-Authorization': str(auth_token)}
    )

    response_json = response.json()
    json_result = json.loads(response_json['Result'])

    team_name = json_result['TeamName']
    members = json_result['Members']
    team_id = json_result['Id']

    member1 = {'name': members[0]['Name'], 'mail': members[0]['Mail'], 'surname': members[0]['Surname']}
    member2 = {'name': members[1]['Name'], 'mail': members[1]['Mail'], 'surname': members[1]['Surname']}
    member3 = {'name': members[2]['Name'], 'mail': members[2]['Mail'], 'surname': members[2]['Surname']}
    member4 = {'name': members[3]['Name'], 'mail': members[3]['Mail'], 'surname': members[3]['Surname']}

    return render(request, 'show_details.html', context={
        'teamname': team_name,
        'team_id': team_id,
        'member1': member1,
        'member2': member2,
        'member3': member3,
        'member4': member4,
    })
