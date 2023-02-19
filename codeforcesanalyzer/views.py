from django.http import HttpResponse
from django.shortcuts import render
import json
from django.utils import timezone
import datetime as dt
import requests
import random
from main.methods import userDetails, submissioncalc, getcontestlist


def home(request):
    return render(request, 'home.html')


def analyze(request):
    userhandle = request.GET.get('text', 'default')

    user = userDetails(userhandle)

    right = submissioncalc(userhandle)[0]
    ce = submissioncalc(userhandle)[1]
    rte = submissioncalc(userhandle)[2]
    tle = submissioncalc(userhandle)[3]
    other = submissioncalc(userhandle)[4]+submissioncalc(userhandle)[5]

    param = {'handle': user['handle'], 'rating': user['rating'], 'user': user, 'rank': user['rank'],
             'maxrating': user['maxRating'], 'titlephoto': user['titlePhoto'], 'avatar': user['avatar'],
             'right': right, 'ce': ce, 'rte': rte, 'tle': tle, 'other': other}
    return render(request, 'analyze.html', param)


def statistics(request):
    return render(request, 'statistics.html')


def compare2(request):
    userhandle1 = request.GET.get('text1', 'default')
    user1 = userDetails(userhandle1)
    right1 = submissioncalc(userhandle1)[0]
    ce1 = submissioncalc(userhandle1)[1]
    rte1 = submissioncalc(userhandle1)[2]
    tle1 = submissioncalc(userhandle1)[3]
    other1 = submissioncalc(userhandle1)[4] + submissioncalc(userhandle1)[5]

    userhandle2 = request.GET.get('text2', 'default')
    user2 = userDetails(userhandle2)
    right2 = submissioncalc(userhandle2)[0]
    ce2 = submissioncalc(userhandle2)[1]
    rte2 = submissioncalc(userhandle2)[2]
    tle2 = submissioncalc(userhandle2)[3]
    other2 = submissioncalc(userhandle2)[4] + submissioncalc(userhandle2)[5]

    param1 = {'handle1': user1['handle'], 'rating1': user1['rating'], 'user1': user1, 'rank1': user1['rank'],
              'maxrating1': user1['maxRating'], 'titlephoto1': user1['titlePhoto'], 'avatar1': user1['avatar'],
              'right1': right1, 'ce1': ce1, 'rte1': rte1, 'tle1': tle1, 'other1': other1,
              'handle2': user2['handle'], 'rating2': user2['rating'], 'user2': user2, 'rank2': user2['rank'],
              'maxrating2': user2['maxRating'], 'titlephoto2': user2['titlePhoto'], 'avatar2': user2['avatar'],
              'right2': right2, 'ce2': ce2, 'rte2': rte2, 'tle2': tle2, 'other2': other2}

    return render(request, 'compare2.html', param1)


def compare(request):
    return render(request, 'compare.html')


def suggest(request):
    return render(request, 'suggest.html')


def contest(request):
    params = getcontestlist()
    return render(request, 'contest.html', params)
