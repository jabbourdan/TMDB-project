import os

import imdb
import requests

from config import TMDB_API_API_V3_auth

def size_str_to_int(self,x):
        return float("inf") if x == 'original' else int(x[1:])
content_temp_path = "./temp_content/"
