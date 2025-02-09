#!/usr/bin/env python3
import requests
import os
import json
import itertools

radarr_api_key=os.environ["radarr_api_key"]
radarr_api_host=os.environ["radarr_api_host"]

radarr_headers = {
    "Accept": "application/json"
}

radarr_session = requests.Session()
radarr_session.headers.update(radarr_headers)

def get_radarr_movie(tmbd_id):
    
    url=f"http://{radarr_api_host}/api/v3/movie/?tmdbId={tmbd_id}&apikey={radarr_api_key}"
    r=radarr_session.get(url)
    data=r.json()
    return data

def update_radarr_movies(data):
    url=f"http://{radarr_api_host}/api/v3/movie/editor?apikey={radarr_api_key}"
    r=radarr_session.put(url, json=data)
    data=r.json()
    return data

radarr_movie_ids_to_update=[]
radarr_movies_to_update=[]

with open('movie_library_content_metadata.json', 'r', encoding='utf-8') as f:
    movie_library_content_metadata=json.load(f)
    for movie in movie_library_content_metadata:
        movie_metadata_guids=movie.get("MediaContainer").get("Metadata")[0].get("Guid")
        for guid in movie_metadata_guids:
            if guid.get("id").startswith("tmdb"):
                tmbd_id = guid.get("id").split("//", 1)[1]
                radarr_movie=get_radarr_movie(tmbd_id)
                radarr_movies_to_update.append(radarr_movie)


radarr_movies=list(itertools.chain.from_iterable(radarr_movies_to_update))
for movie in radarr_movies:
    radarr_movie_ids_to_update.append(movie.get("movieFile").get("movieId"))
data_payload_movie_editor_request={
        "rootFolderPath": "NEWFOLDERPATHHERE",
        "moveFiles": True,
        "movieIds": radarr_movie_ids_to_update
}

with open('radarr_movies_to_update.json', 'w', encoding='utf-8') as f:
    json.dump(radarr_movies_to_update, f, ensure_ascii=False, indent=4)
print("File written successfully, items in radarr_movies_to_update.json: ", len(radarr_movies_to_update))
with open('radarr_movie_ids_to_update.json', 'w', encoding='utf-8') as f:
    json.dump(radarr_movie_ids_to_update, f, ensure_ascii=False, indent=4)
print("File written successfully, items in radarr_movie_ids_to_update.json: ", len(radarr_movie_ids_to_update))
with open('data_payload_movie_editor_request.json', 'w', encoding='utf-8') as f:
    json.dump(data_payload_movie_editor_request,f , ensure_ascii=False)
print("File written successfully, items in data_payload_movie_editor_request.json for key movieIds: ", len(radarr_movie_ids_to_update))

print(update_radarr_movies(data_payload_movie_editor_request))