from django.http import HttpResponse
from django.shortcuts import render
import json
from django.utils import timezone
import datetime as dt
import requests
import random
from main.methods import userDetails, submissioncalc,getcontestlist





def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def analyze(request):
    userhandle = request.GET.get('text', 'default')

    user = userDetails(userhandle)

    count = submissioncalc(userhandle)[0]
    wrong = submissioncalc(userhandle)[1]

    param = {'handle': user['handle'], 'rating': user['rating'], 'user': user, 'rank': user['rank'],
             'maxrating': user['maxRating'], 'titlephoto': user['titlePhoto'], 'avatar': user['avatar'],
             'right': count, 'wrong': wrong}
    return render(request, 'analyze.html', param)


def statistics(request):
    return render(request, 'statistics.html')


def compare2(request):
    userhandle1 = request.GET.get('text1', 'default')
    user1 = userDetails(userhandle1)
    count1 = submissioncalc(userhandle1)[0]
    wrong1 = submissioncalc(userhandle1)[1]

    userhandle2 = request.GET.get('text2', 'default')
    user2 = userDetails(userhandle2)
    count2 = submissioncalc(userhandle2)[0]
    wrong2 = submissioncalc(userhandle2)[1]

    param1 = {'handle1': user1['handle'], 'rating1': user1['rating'], 'user1': user1, 'rank1': user1['rank'],
              'maxrating1': user1['maxRating'], 'titlephoto1': user1['titlePhoto'], 'avatar1': user1['avatar'],
              'right1': count1, 'wrong1': wrong1,
              'handle2': user2['handle'], 'rating2': user2['rating'], 'user2': user2, 'rank2': user2['rank'],
              'maxrating2': user2['maxRating'], 'titlephoto2': user2['titlePhoto'], 'avatar2': user2['avatar'],
              'right2': count2, 'wrong2': wrong2}

    return render(request, 'compare2.html', param1)


def compare(request):
    return render(request, 'compare.html')


def suggest(request):
    return render(request, 'suggest.html')


def contest(request):

    params = getcontestlist()
    return render(request, 'contest.html', params)
