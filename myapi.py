from flask import Flask, request, json
import requests
from base64 import b64encode

response_counter = 0


app = Flask(__name__)


def Enter_inbetween(data):
    if Not_run():
        return 0

    print('bruv')
    stop_time = data['created_at']
    start_time = Find_staring_time()
    print(stop_time - start_time)


    time_entry_details = {
        "id": 2569204358,
        "workspace_id": 5437043,
        "project_id": 174485519,
        "created_with": "broom",
        "billable": False,
        "start": start_time,
        "stop": stop_time,
        "description": "Inbetween",
        "duronly": False,
        "at": "2022-07-13T17:47:28+00:00",
        "user_id": 6937981,
        "uid": 6937981,
        "wid": 5437043,
        "pid": 174485519
    }


    check = requests.post('https://api.track.toggl.com/api/v9/workspaces/5437043/time_entries', headers={
                  'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(b"33cce6439bbe33e40221831f1e7cef23:api_token").decode("ascii")},json= time_entry_details)
    print(check)

    return 0


def Find_staring_time():
    resp = requests.get('https://api.track.toggl.com/api/v9/me/time_entries', headers={
                        'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(b"33cce6439bbe33e40221831f1e7cef23:api_token").decode("ascii")})
    return resp.json()[1]['stop']

def Not_run():
    resp = requests.get('https://api.track.toggl.com/api/v9/me/time_entries', headers={
                        'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(b"33cce6439bbe33e40221831f1e7cef23:api_token").decode("ascii")})
    return resp.json()[1]['description'] == "Inbetween"

@ app.route('/')
def hello():
    return 'Fuck me'


@ app.route('/Togglhooks', methods=['POST'])
def get_response():
    global response_counter
    response_counter += 1
    print('The number of reponses is {} '.format(response_counter))
    data = request.json
    if(data['event_id'] != 0) :
        Enter_inbetween(data)
    return data


if __name__ == '__main__':
    app.run(debug=True)
