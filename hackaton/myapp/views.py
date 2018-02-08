from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        teamname = request.POST.get('Teamname')
        password = request.POST.get('Password')

        team_member = {}
        team_member[0] = {
            'name':request.POST.get('Name1'),'surname':request.POST.get('Surname1'),'':request.POST.get('email1')
            }
        team_member[0] = {
            'name':request.POST.get('Name2'),'surname':request.POST.get('Surname2'),'':request.POST.get('email2')
            }
        team_member[0] = {
            'name':request.POST.get('Name3'),'surname':request.POST.get('Surname3'),'':request.POST.get('email3')
            }

        team_member[0] = {
            'name':request.POST.get('Name4'),'surname':request.POST.get('Surname4'),'':request.POST.get('email4')
        }

        print(teamname)
        print(password)
        print(team_member)

    return render(request, 'index.html')
