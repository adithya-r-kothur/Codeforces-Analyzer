from django.http import HttpResponse
from django.shortcuts import render
import json
from django.utils import timezone
import datetime as dt
import requests
import random


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def analyze(request):
    userhandle = request.GET.get('text', 'default')
    url = requests.get(
        'https://codeforces.com/api/user.info?handles=' + userhandle)
    jsonData = url.json()
    data = json.dumps(jsonData)
    codeforcesHandle = json.loads(data)
    if codeforcesHandle['status'] != "OK":
        return False

    user = codeforcesHandle['result'][0]

    param = {'handle': user['handle'], 'firstname': user['firstName'], 'rating': user['rating'], 'user': user, 'rank': user['rank'], 'maxrating': user['maxRating'], 'titlephoto': user['titlePhoto'], 'country': user['country'], 'avatar': user['avatar']}
    return render(request, 'analyze.html', param)


def statistics(request):
    return render(request, 'statistics.html')


def compare(request):
    return render(request, 'compare.html')


def suggest(request):
    return render(request, 'suggest.html')
