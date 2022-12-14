
## TMDB-project :

- β¨ This project ask the user to search for a movie poster and give him the poster for this movie
- πΎ All the posters that the user want will save in mongoDB and he can delete it or update it
- π½ All this project will be in container and I will use docker-compose to use also the image of mongoDB
- π Build a simple web app that use a API for TMDB to download the posters

## Features

- Take a poster movie
- Database for posters that you ask
- Full control of the DataBase (CRUD)


## Technologies
- π Bash-scripting
- β­ Python 
- π« Docker
- β  Docker-compose
- πΊοΈ Flask
- π» OOP
- π±  Web API (TMDB)
- πΉοΈ Mongodb
- π Git

## requirements

- π±  API key for imdb (Steps to make a new one in workflow)
- πΊοΈ Docker
- π Code editor

## WorkFlow
- π¨βπ» Clone this project to your local PC (git clone https://github.com/jabbourdan/TMDB-project.git)


- π after cloning you need to have a TMDB API you can follow the stepts below:
        

        1. Go to https://www.themoviedb.org/ and create new account
        2. Go to settings and click on API
        3. Generate new API V3  
        
- π± Open the project that you clone in step 1 

        make new file with name config.py and copy in the API key that you genrate in step 2


- π« Install docker to your computer and go to the project that you clone then open a terminal (After you added the config file) :

        docker-compsoe -f docker-compose.yml up

- π½ After few seconds will you see the IP link that you can access the code with it (like the photo below)



![Capture](https://user-images.githubusercontent.com/111487226/205933927-c6b007b8-448b-4ef1-b5a3-e60d4cffeb49.PNG)

- π¨βπ» You will see this page you can choise if you want to search for a new posters ,delete a poster in data base that you searched for and update a photo name in database

![main page1](https://user-images.githubusercontent.com/111487226/207348363-19d3c2bb-919d-4a22-81c1-0ea2e54e244c.png)

- β² example of search for The Matrix :

![example of search](https://user-images.githubusercontent.com/111487226/207348702-457b4f0d-ecb3-4d3f-8b79-486d9e04569b.png)

- π Output:

![example of photo](https://user-images.githubusercontent.com/111487226/207348873-388a9889-03de-4861-8446-53a2ab2027da.png)
