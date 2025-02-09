#!/usr/bin/env python3
import requests
import os
import json

plex_api_key=os.environ["plex_api_key"]
plex_api_host=os.environ["plex_api_host"]

plex_headers = {
    "Accept": "application/json"
}

plex_session = requests.Session()
plex_session.headers.update(plex_headers)

def list_plex_libraries():
    
    url=f"http://{plex_api_host}/library/sections?X-Plex-Token={plex_api_key}"
    r=plex_session.get(url)
    data=r.json()
    return data

def get_plex_library(section_id):
    
    url=f"http://{plex_api_host}/library/sections/{section_id}?X-Plex-Token={plex_api_key}"
    r=plex_session.get(url)
    data=r.json()
    return data

def list_plex_library_content(section_id,tag):
    
    url=f"http://{plex_api_host}/library/sections/{section_id}/{tag}?X-Plex-Token={plex_api_key}"
    r=plex_session.get(url)
    data=r.json()
    return data

def get_plex_library_item_metadata(rating_key):
    url=f"http://{plex_api_host}/library/metadata/{rating_key}?X-Plex-Token={plex_api_key}"
    r=plex_session.get(url)
    data=r.json()
    return data

libraries=list_plex_libraries()
movie_library_content_metadata=[]
label_id="35069"

for library in libraries["MediaContainer"]["Directory"]:

    if library["title"] == "Movies":
        movie_library_id=library["key"]
        movie_library_content=list_plex_library_content(movie_library_id,"unwatched")
        for movie in movie_library_content["MediaContainer"]["Metadata"]:
           item=get_plex_library_item_metadata(movie["ratingKey"])
           item_metadata_label=item.get("MediaContainer").get("Metadata")[0].get("Label")
           if item_metadata_label != None:
                item_metadata_label_id=str(item_metadata_label[0].get("id"))
                if item_metadata_label_id == label_id:
                    movie_library_content_metadata.append(item)

with open('movie_library_content_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(movie_library_content_metadata, f, ensure_ascii=False, indent=4)
print("Filtered labelled media exported to movie_library_content_metadata.json, content size is "+str(len(movie_library_content_metadata)))
