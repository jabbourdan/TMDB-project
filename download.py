import os

import imdb
import requests

from config import TMDB_API_API_V3_auth

def size_str_to_int(x):
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
        self.movie_id = ''
        self.movie_name = ''
        self.content_temp_path = "./temp_content/"    
    
    def size_str_to_int(self,x):
            return float("inf") if x == 'original' else int(x[1:])

    def _get_json(self,url):
        r = requests.get(url)
        return r.json()

    def _download_images(self,urls,path='.'):
                
        r = requests.get(urls[0])
        filetype = r.headers['content-type'].split('/')[-1]
        filename = '{0}.{1}'.format(self.movie_name, filetype)
        filepath = os.path.join(self.content_temp_path , filename)
        with open(filepath,'wb') as w:
            w.write(r.content)
        
    def get_poster_urls(self,imdbid):
        """ return image urls of posters for IMDB id
            returns all poster images from 'themoviedb.org'. Uses the
            maximum available size. 
            Args:
                imdbid (str): IMDB id of the movie
            Returns:
                list: list of urls to the images
        """
        config = self._get_json(self.CONFIG_PATTERN.format(key=self.KEY))
        base_url = config['images']['base_url']
        sizes = config['images']['poster_sizes']

       
        #sizes' should be sorted in ascending order, so
        self.max_size = sizes[-1]
        #should get the largest size as well.        
       
        posters = self._get_json(self.IMG_PATTERN.format(key=self.KEY,imdbid=imdbid))['posters']
        poster_urls = []
        for poster in posters:
            rel_path = poster['file_path']
            url = "{0}{1}{2}".format(base_url, self.max_size, rel_path)
            poster_urls.append(url) 

        return poster_urls
    
        
        
    def get_movie_id(self):
        res = self._get_json(f'https://api.themoviedb.org/3/search/movie?api_key={self.KEY}&query={self.movie_name}')
        first_result = res['results']
        #print('Response =>', first_result)
        #self.movie_name = first_result[0]['original_title']           
        self.movie_id = first_result[0]['id']
        return self.movie_id

    def tmdb_poster_name(self,movie_name, count=1, outpath='.'):
        self.movie_name = movie_name
        self.get_movie_id()
        urls = self.get_poster_urls(self.movie_id)
        if count is not None:
            urls = urls[:count]
        self._download_images(urls, outpath)
