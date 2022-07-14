import requests
from base64 import b64encode

ob = [{}]
    

for js in ob:
    requests.delete('https://api.track.toggl.com/api/v9/workspaces/5437043/time_entries/{}'.format(js['id']), headers={'content-type': 'application/json', 'Authorization': 'Basic %s' % b64encode(
    b"33cce6439bbe33e40221831f1e7cef23:api_token").decode("ascii")})


