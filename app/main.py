from typing import Union
from ytmusicapi import YTMusic
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

ytmusic = YTMusic('oauth.json')
app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/search')
def search(q, f):   
    return ytmusic.search(q, f)


@app.get('/search_recommend')
def search_recommend(q):
    search_recommend = ytmusic.get_search_suggestions(q)    
    return search_recommend

@app.get('/song/{videoId}')
def get_song(videoId):    
    song = ytmusic.get_song(videoId)
    return song