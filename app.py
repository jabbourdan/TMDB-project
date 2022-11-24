from flask import Flask, render_template, request

from download import imdb1
from mongoDB import mongoDB

app = Flask(__name__)
#mongo = mongoDB("localhost", 27017)
mongo = mongoDB("db_host", 27017)


@app.route("/search", methods=['GET','POST'])
def search():
    if(request.method == 'POST'):
        data = request.form
        name_movie = data['name']
        if(mongo.search(name_movie)):
            mongo.read_data(name_movie)
        else:
            imdb = imdb1()
            imdb.tmdb_poster_name(name_movie)
            mongo.upload()
            mongo.read_data(name_movie + '1')
        return "The image has downloaded "
    return render_template("insert.html")

@app.route("/delete", methods=['GET','POST'])
def delete():
    if(request.method == 'POST'):
        dele = request.form
        print(dele)
        name = dele['name']
        #print(arg)
        if(mongo.search(name) or name == "all"):
            return mongo.delete(name)
        else:
            return "There is no image like this name "
    return render_template("delete.html")

@app.route("/update", methods=['GET','POST'])
def update():
    if(request.method == 'POST'):
        update = request.form
        movie_name = update['movie_name']
        key_to_update = update['key_to_update']
        val_to_update = update['val_to_update']
        return mongo.update(movie_name,key_to_update,val_to_update)
    return render_template("update.html") 

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("base.html") 

if __name__ == '__main__':
    app.run(port=5001,host = '0.0.0.0' , debug = True) 
