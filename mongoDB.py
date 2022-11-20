import os

import gridfs
from pymongo import MongoClient


class mongoDB():
    def __init__(self,ip,port):
        self.db = self.mongo_conn(ip,port)
        self.database 
        self.fs = gridfs.GridFS(self.db)
        
    def mongo_conn(self,ip ,port):
        try:
            conn = MongoClient(ip ,port)
            self.database = conn["movies"]
            return self.database
        except Exception as e:
            print("error in mongoDB connection ")
