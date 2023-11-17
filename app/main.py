from typing import Union
from ytmusicapi import YTMusic
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

ytmusic = YTMusic('oauth.json')
app = FastAPI()

print(os.environ.get('ORIGIN'))

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ.get('ORIGIN'),
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/search')
def search(q, f):
    if (f == ''):
        return ytmusic.search(q)
    else:
        return ytmusic.search(q, f)


@app.get('/search_recommend')
def search_recommend(q):
    search_recommend = ytmusic.get_search_suggestions(q)
    return search_recommend


@app.get('/song/{videoId}')
def get_song(videoId):
    song = ytmusic.get_song(videoId)
    return song
