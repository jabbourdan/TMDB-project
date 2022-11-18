import os

import imdb
import requests

from config import TMDB_API_API_V3_auth

def size_str_to_int(self,x):
        return float("inf") if x == 'original' else int(x[1:])
content_temp_path = "./temp_content/"

class imdb1():
    def __init__(self):
        self.CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
        self.IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}' 
        self.KEY = TMDB_API_API_V3_auth
        self.url = self.CONFIG_PATTERN.format(key=self.KEY)
        self.config = requests.get(self.url).json()
        self.sizes = self.config['images']['poster_sizes']
        self.max_size = max(self.sizes, key=size_str_to_int)
        self.imdb_id = ''
        self.name = ''
        self.content_temp_path = "./temp_content/"    
        
    def _get_json(self,url):
        r = requests.get(url)
        return r.json()
