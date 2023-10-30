from ytmusicapi import YTMusic
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

ytmusic = YTMusic('oauth.json')
app = FastAPI()

origins = [
    'http://localhost:5173',
    'http://144.24.84.244:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/search')
def search(q):    
    search_results = ytmusic.search(q)    
    return search_results

@app.get('/search_recommend')
def search_recommend(q):
    search_recommend = ytmusic.get_search_suggestions(q)    
    return search_recommend
    