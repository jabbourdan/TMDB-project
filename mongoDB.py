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
            
    def upload(self):
        for filename in os.listdir("./temp_content"):
            with open(os.path.join("./temp_content/", filename), 'r') as f:
                #db = mongo_conn()
                file_location = "./temp_content/" + filename
                file_data = open(file_location, "rb")
                data = file_data.read()
                fs = gridfs.GridFS(self.db)
                fs.put(data, filename = filename)
                print("upload completed")
