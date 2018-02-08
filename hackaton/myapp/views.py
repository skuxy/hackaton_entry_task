from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    teamname = request.POST.get('teamname')
    password = request.POST.get('password')
    team_member = list()
    for i in range(4):
        team_member[i] = [request.POST.get('name'),request.POST.get('surname'),request.POST.get('mail')]

    # response = JsonResponse({'teamname':teamname,'password':password})

    return render(request, 'index.html')
