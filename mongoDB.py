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
        with open(os.path.join("./temp_content/", filename), 'r') as f:
            file_location = "./temp_content/" + filename
            file_data = open(file_location, "rb")
            data = file_data.read()
            fs = gridfs.GridFS(self.db)
            fs.put(data, filename = filename)
            print("upload completed")
                
    def search(self,filename):
        filename = filename + '.jpeg'
        mycol = self.db["fs.files"]
        statment = False 
        for x in mycol.find():
            if(filename == x['filename']):
                statment = True
                return statment 
        return statment
    
    
    def update(self,movie_name,key_to_update,val_to_update):
        file_id=self.search_image_file_id_by_name((movie_name))
        movie_name = movie_name + ".jpeg"
        mycol = self.database["fs.files"]
        myquery = {"_id": file_id}
        new_values = {"$set": {key_to_update: val_to_update + '.jpeg'}}
        db_update_response=mycol.update_one(myquery, new_values)
        output = {'Status': 'Successfully Updated' if db_update_response.modified_count > 0 else "Nothing was updated."}
        return output

    def search_image_file_id_by_name(self, movie_name):
        if(self.search(movie_name)):
            return self.fs.find_one({"filename": movie_name + '.jpeg'})._id

        else:
            print("The image not her")
            
    def read_data(self,filename):

        if(self.search(filename)):
            image_bin = self.fs.get_last_version(filename + '.jpeg').read()
            with open(f'{filename}.jpeg','wb') as outfile:
                image = outfile.write(image_bin)
            return image
        else:
            return "The image not found"

    def delete(self,filename):
        mycol = self.db["fs.files"]
        if(filename == 'all'):
            mycol.delete_many({})
            return "All the images has deleted"
        else:
            mycol.delete_many({"filename" : filename + '.jpeg'})
            return "The " + filename + ' deleted'
