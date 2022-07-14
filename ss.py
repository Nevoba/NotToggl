from pickle import NONE
import requests
from base64 import b64encode
from flask import Flask, request, json


stop_time = '2022-07-13T16:41:59+00:00'
start_time = '2022-07-13T16:41:00+00:00'

time_entry_details =    {
        "id": 2569204358,
        "workspace_id": 5437043,
        "project_id": 174485519,
        "created_with": "broom",
        "billable": False,
        "start": start_time,
        "stop": stop_time,
        "duration": 146,
        "description": "Inbetween",
        "duronly": False,
        "at": "2022-07-13T17:47:28+00:00",
        "user_id": 6937981,
        "uid": 6937981,
        "wid": 5437043,
        "pid": 174485519
    }


# time_entry_details = """
#     "billable": "False",
#     "description": "Inbetween",
#     "start": "2022-07-13T16:41:00+00:00",
#     "stop": "2022-07-13T16:41:59+00:00",
#     "wid": "5437043",
#     "workspace_id": "5437043'}"""

print('here we go')

# respon = requests.post('https://api.track.toggl.com/api/v9/workspaces/5437043/time_entries', headers={'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(
#     b"33cce6439bbe33e40221831f1e7cef23:api_token").decode("ascii")}, json = time_entry_details)

respon = requests.get('https://api.track.toggl.com/api/v9/me/time_entries', headers={'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(
    b"33cce6439bbe33e40221831f1e7cef23:api_token").decode("ascii")})


print(respon.text)
