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
        self.imdb_id = ''
        self.name = ''
        self.content_temp_path = "./temp_content/"    
    
    def size_str_to_int(self,x):
            return float("inf") if x == 'original' else int(x[1:])

    def _get_json(self,url):
        r = requests.get(url)
        return r.json()

    def _download_images(self,urls,path='.'):
                
        r = requests.get(urls[0])
        filetype = r.headers['content-type'].split('/')[-1]
        filename = '{0}.{1}'.format(self.name, filetype)
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

        """
            'sizes' should be sorted in ascending order, so
                max_size = sizes[-1]
            should get the largest size as well.        
        """
        posters = self._get_json(self.IMG_PATTERN.format(key=self.KEY,imdbid=imdbid))['posters']
        poster_urls = []
        for poster in posters:
            rel_path = poster['file_path']
            url = "{0}{1}{2}".format(base_url, self.max_size, rel_path)
            poster_urls.append(url) 

        return poster_urls

    def tmdb_poster_name(self,name, count=1, outpath='.'):
        self.name = name
        ia = imdb.IMDb()
        for i in range(0,10):
            items = ia.search_movie(name)
            if(len(items)==0):
                items = ia.search_movie(name)
                i = i + 1
            else:
                break
        self.imdb_id = "tt" + str(items[0].movieID)
        urls = self.get_poster_urls(self.imdb_id)
        if count is not None:
            urls = urls[:count]
        self._download_images(urls, outpath)
