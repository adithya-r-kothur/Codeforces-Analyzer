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
    url1 = requests.get('https://codeforces.com/api/user.status?handle=' + userhandle)
    jsonData1 = url1.json()
    data1 = json.dumps(jsonData1)

    submissions = json.loads(data1)
    submissions = submissions['result']
    if codeforcesHandle['status'] != "OK":
        return False

    user = codeforcesHandle['result'][0]

    count = 0
    wrong = 0
    print(len(submissions))
    for problem in submissions:
        if problem['verdict'] == "OK":
            count = count + 1
        else:
            wrong = wrong + 1

    param = {'handle': user['handle'], 'rating': user['rating'], 'user': user, 'rank': user['rank'],
             'maxrating': user['maxRating'], 'titlephoto': user['titlePhoto'], 'avatar': user['avatar'],
             'right': count, 'wrong': wrong}
    return render(request, 'analyze.html', param)


def statistics(request):
    return render(request, 'statistics.html')


def compare2(request):
    userhandle1 = request.GET.get('text1', 'default')
    url1 = requests.get(
        'https://codeforces.com/api/user.info?handles=' + userhandle1)
    jsonData1 = url1.json()
    data1 = json.dumps(jsonData1)
    codeforcesHandle1 = json.loads(data1)
    if codeforcesHandle1['status'] != "OK":
        return False
    user1 = codeforcesHandle1['result'][0]

    url12 = requests.get('https://codeforces.com/api/user.status?handle=' + userhandle1)
    jsonData12 = url12.json()
    data12 = json.dumps(jsonData12)

    submissions = json.loads(data12)
    submissions = submissions['result']

    count1 = 0
    wrong1 = 0

    for problem in submissions:
        if problem['verdict'] == "OK":
            count1 = count1 + 1
        else:
            wrong1 = wrong1 + 1

    userhandle2 = request.GET.get('text2', 'default')
    url2 = requests.get(
        'https://codeforces.com/api/user.info?handles=' + userhandle2)
    jsonData2 = url2.json()
    data2 = json.dumps(jsonData2)
    codeforcesHandle2 = json.loads(data2)
    if codeforcesHandle2['status'] != "OK":
        return False
    user2 = codeforcesHandle2['result'][0]

    url22 = requests.get('https://codeforces.com/api/user.status?handle=' + userhandle2)
    jsonData22 = url22.json()
    data22 = json.dumps(jsonData22)

    submissions2 = json.loads(data22)
    submissions2 = submissions2['result']

    count2 = 0
    wrong2 = 0

    for problem in submissions2:
        if problem['verdict'] == "OK":
            count2 = count2 + 1
        else:
            wrong2 = wrong2 + 1

    param1 = {'handle1': user1['handle'], 'rating1': user1['rating'], 'user1': user1, 'rank1': user1['rank'],
              'maxrating1': user1['maxRating'], 'titlephoto1': user1['titlePhoto'], 'avatar1': user1['avatar'],'right1': count1, 'wrong1': wrong1,
              'handle2': user2['handle'], 'rating2': user2['rating'], 'user2': user2, 'rank2': user2['rank'],
              'maxrating2': user2['maxRating'], 'titlephoto2': user2['titlePhoto'], 'avatar2': user2['avatar'],'right2': count2, 'wrong2': wrong2}

    return render(request, 'compare2.html', param1)


def compare(request):
    return render(request, 'compare.html')


def suggest(request):
    return render(request, 'suggest.html')
