import os

import gridfs
from pymongo import MongoClient


class mongoDB():
    def __init__(self,ip,port):
        self.db = self.mongo_conn(ip,port)
        self.database 
        self.fs = gridfs.GridFS(self.db)
