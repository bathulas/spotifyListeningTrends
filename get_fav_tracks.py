import json
import time
import requests

offset = 0
limit = 50
total_tracks = []

def get_fav_tracks(url, offset, limit):
    token = "{token}"
#your token goes here
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
    response = get("https://api.spotify.com/v1/me/tracks", offset, limit)
