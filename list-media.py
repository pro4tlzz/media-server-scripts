#!/usr/bin/env python3
from msilib.schema import Directory
from operator import ge
import requests
import os

tautulli_api_key=os.environ['tautulli_api_key']
tautulli_api_host=os.environ['tautulli_api_host']
plex_api_key=os.environ['plex_api_key']
plex_api_host=os.environ['plex_api_host']

tautulli_headers = {
    'Accept': 'application/json'
}

tautulli_session = requests.Session()
tautulli_session.headers.update(tautulli_headers)


plex_headers = {
    'Accept': 'application/json'
}

plex_session = requests.Session()
plex_session.headers.update(plex_headers)

def get_activity():

    url=f"{tautulli_api_host}/api/v2?apikey={tautulli_api_key}&cmd=get_activity"
    print(url)
    response=tautulli_session.get(url)
    response.raise_for_status
    api_response=response.json()
    data=api_response['response']['data']['sessions']

    for each in data:
        print(each['user'],each['title'])

def get_library_content(section_id):

    url=f"{tautulli_api_host}/api/v2?apikey={tautulli_api_key}&cmd=get_library&section_id={section_id}"
    print(url)
    response=tautulli_session.get(url)
    response.raise_for_status
    api_response=response.json()
    print(api_response)

def get_libraries():

    url=f"{tautulli_api_host}/api/v2?apikey={tautulli_api_key}&cmd=get_libraries"
    print(url)
    response=tautulli_session.get(url)
    response.raise_for_status
    api_response=response.json()
    data=api_response['response']['data']
    for each in data:
        section_id=each['section_id']
        get_library_content(section_id)

def list_plex_library():
    
    url=f"{plex_api_host}/library/sections?X-Plex-Token={plex_api_key}"
    print(url)
    response=plex_session.get(url)
    api_response=response.json()
    print(api_response)
    directory=api_response['directory']

get_activity()
#list_plex_library()
get_libraries()