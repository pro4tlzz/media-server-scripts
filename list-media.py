#!/usr/bin/env python3
from operator import ge
import requests
import os

tautulli_api_key=os.environ['tautulli_api_key']
tautulli_api_host=os.environ['tautulli_api_host']

tautulli_headers = {
    'Accept': 'application/json'
}

tautulli_session = requests.Session()
tautulli_session.headers.update(tautulli_headers)

def get_activity():

    url=f"{tautulli_api_host}/api/v2?apikey={tautulli_api_key}&cmd=get_activity"
    print(url)
    response=tautulli_session.get(url)
    api_response=response.json()
    data=api_response['response']['data']['sessions']

    for each in data:
        print(each['user'],each['title'])

get_activity()