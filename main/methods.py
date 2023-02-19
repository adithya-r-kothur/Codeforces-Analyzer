import json
from django.utils import timezone
import datetime as dt
import requests
import random


def unixtime_to_indiantime(unixtime):
    # Convert Unix time to UTC datetime object
    utc_datetime = dt.datetime.utcfromtimestamp(unixtime)

    # Convert UTC datetime to Indian Standard Time (IST) datetime object
    ist_offset = dt.timedelta(hours=5, minutes=30)  # IST is 5 hours 30 minutes ahead of UTC
    ist_datetime = utc_datetime + ist_offset

    # Format IST datetime as a string and return it
    return ist_datetime.strftime('%Y-%m-%d %H:%M:%S')


def convertToHour(secondsTime):
    return str(dt.timedelta(seconds=secondsTime))


def convertUnixTime(unixtime):
    date = dt.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d')
    time = dt.datetime.fromtimestamp(unixtime).strftime('%H:%M:%S')
    date_time_obj = dt.datetime.strptime(date + " " + time, '%Y-%m-%d %H:%M:%S')
    time = date_time_obj.time()
    time = str((dt.datetime.combine(dt.date(1, 1, 1), time) +
                dt.timedelta(hours=5, minutes=30)).time())
    return date + " " + time


def userDetails(codeforcesHandle):
    url = requests.get(
        'https://codeforces.com/api/user.info?handles=' + codeforcesHandle)
    jsonData = url.json()
    data = json.dumps(jsonData)
    codeforcesHandle = json.loads(data)
    if codeforcesHandle['status'] != "OK":
        return False

    return codeforcesHandle['result'][0]


def submissioncalc(userhandle):
    url1 = requests.get(
        'https://codeforces.com/api/user.status?handle=' + userhandle)
    jsonData1 = url1.json()
    data1 = json.dumps(jsonData1)

    submissions = json.loads(data1)
    submissions = submissions['result']
    count = 0
    wrong = 0
    print(len(submissions))
    for problem in submissions:
        if problem['verdict'] == "OK":
            count = count + 1
        else:
            wrong = wrong + 1
    ans = [wrong, count]
    return ans


def getcontestlist():
    contestli = requests.get('https://codeforces.com/api/contest.list?gym=false')
    contestsjson = contestli.json()
    contestsdata = json.dumps(contestsjson)

    contests = json.loads(contestsdata)

    one = contests['result'][4]
    one['startTimeSeconds'] = unixtime_to_indiantime(one['startTimeSeconds'])
    one['durationSeconds'] = convertToHour(one['durationSeconds'])

    two = contests['result'][3]
    two['startTimeSeconds'] = unixtime_to_indiantime(two['startTimeSeconds'])
    two['durationSeconds'] = convertToHour(two['durationSeconds'])

    three = contests['result'][2]
    three['startTimeSeconds'] = unixtime_to_indiantime(three['startTimeSeconds'])
    three['durationSeconds'] = convertToHour(three['durationSeconds'])

    four = contests['result'][1]
    four['startTimeSeconds'] = unixtime_to_indiantime(four['startTimeSeconds'])
    four['durationSeconds'] = convertToHour(four['durationSeconds'])

    five = contests['result'][0]
    five['startTimeSeconds'] = unixtime_to_indiantime(five['startTimeSeconds'])
    five['durationSeconds'] = convertToHour(five['durationSeconds'])

    params = {

        'name1': one['name'],
        'id1': one['id'],
        'start1': one['startTimeSeconds'],
        'duration1': one['durationSeconds'],

        'name2': two['name'],
        'id2': two['id'],
        'start2': two['startTimeSeconds'],
        'duration2': two['durationSeconds'],

        'name3': three['name'],
        'id3': three['id'],
        'start3': three['startTimeSeconds'],
        'duration3': three['durationSeconds'],

        'name4': four['name'],
        'id4': four['id'],
        'start4': four['startTimeSeconds'],
        'duration4': four['durationSeconds'],

        'name5': five['name'],
        'id5': five['id'],
        'start5': five['startTimeSeconds'],
        'duration5': five['durationSeconds']
    }

    return params
