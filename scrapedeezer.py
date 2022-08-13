import os
import sys
import requests
import re
import os

def get_artist_id(band_name):
    api_response = requests.get("https://api.deezer.com/search/artist?q="+band_name).json()
    artist_id = None
    while artist_id == None:
        for artist in api_response["data"]:
            if artist["name"] == band_name:
                artist_id = artist["id"]
                break
        if "next" in api_response.keys():
            api_response = requests.get(api_response["next"]).json()
        else:
            break
    return artist_id

def get_album_covers(artist_id):
    global imageno
    api_response = requests.get("https://api.deezer.com/artist/"+str(artist_id)+"/albums"+"?limit=1000").json()
    for album in api_response["data"]:
        if album["genre_id"] == 152 or album["genre_id"] == 464:
            coverart = album["cover_big"]
            print(coverart)
            file = open("F:/Game project/album covers/album" + str(imageno) + ".jpg", "wb")
            file.write(requests.get(coverart).content)
            file.close()
            imageno += 1


f = open('C:/Users/PCP/Desktop/game/bandlist.txt', "r", encoding="utf-8")
x = f.read()
bandlist = x.split(", ")

imageno = 2392

for band_name in bandlist[1018:]:
    try:
        print(band_name)
        artist_id = get_artist_id(band_name)
        print(artist_id)
        if artist_id != None:
            get_album_covers(artist_id)
    except:
        continue