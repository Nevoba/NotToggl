from wsgiref import headers
import requests
from base64 import b64encode
import webhooks

user_id = 6937981
my_worksapce_id = 5437043
subscription_id = 315


URI = {'Webhook':'https://api.track.toggl.com/webhooks/api/v1/subscriptions/{}', 'Time entries':'https://api.track.toggl.com/api/v9/me/time_entries','Organizations': 'https://api.track.toggl.com/api/v9/organizations'}
URL_callback = 'https://9e47-2a06-c701-40ef-7b00-3d74-82dc-f1f2-9611.eu.ngrok.io/Togglhooks'
headers_api = {'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"33cce6439bbe33e40221831f1e7cef23:api_token").decode("ascii")}
json_api = """
    "url_callback": "{}", 
    "enabled": true, 
    "description": "Nevo's first webhook"
"""

# headers_api = {'content-type': 'application/json', 'Authorization' : 'Basic %s' %  b64encode(b"33cce6439bbe33e40221831f1e7cef23:api_token").decode("ascii")}
# json_api = ''



 # data = requests.post(URI['Webhook'].format(my_worksapce_id), headers=headers_api, json=json_api.format(URL_callback)) 
data = requests.post('https://api.track.toggl.com/webhooks/api/v1/subscriptions/5437043', headers=headers_api) 

print(data.text)

