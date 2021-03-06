#!/usr/bin/python3
import json
import time
import requests

offset = 0
limit = 50
total_tracks = []

def get_data(url, offset, limit):
    token = "{token}"
#Your token goes here
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }
    req = requests.get(url,params={"offset":str(offset), "limit":str(limit)}, headers=headers)
    return req.json()
    
response  = get("https://api.spotify.com/v1/me/tracks", offset, limit)
while len(response["items"]) > 0:
    time.sleep(1)
    offset += limit
    total.append(response)
    response = get_data("https://api.spotify.com/v1/me/tracks", offset, limit)
# Get audio features of favorite tracks
track_ids = [[(track['added_at'],track['track']['id']) for track in x['items']]   for x in total]
id_strings = ["%2C".join([x[1] for x in id_list_]) for id_list_ in track_ids]
counter= 0
track_features_ = []
while (counter+1) < len(id_strings):
    counter += 1
    time.sleep(0.6)
    resp = get_data("https://api.spotify.com/v1/audio-features?ids=" + id_strings[counter],0,0)
    track_features_.append(resp)
