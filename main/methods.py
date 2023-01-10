import json
from django.utils import timezone
import datetime as dt
import requests
import random


def userDetails(codeforcesHandle):
    url = requests.get(
        'https://codeforces.com/api/user.info?handles=' + codeforcesHandle)
    jsonData = url.json()
    data = json.dumps(jsonData)
    codeforcesHandle = json.loads(data)
    if codeforcesHandle['status'] != "OK":
        return False

    return codeforcesHandle['result'][0]
