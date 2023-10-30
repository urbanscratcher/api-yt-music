from ytmusicapi import YTMusic
from fastapi import FastAPI

ytmusic = YTMusic('oauth.json')
app = FastAPI()

@app.get('/search')
def search(q):    
    search_results = ytmusic.search(q)    
    return search_results

@app.get('/search_recommend')
def search_recommend(q):
    search_recommend = ytmusic.get_search_suggestions(q)    
    return search_recommend
    