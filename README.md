
## TMDB-project :

- ✨ This project ask the user to search for a movie poster and give him the poster for this movie
- 💾 All the posters that the user want will save in mongoDB and he can delete it or update it
- 💽 All this project will be in container and I will use docker-compose to use also the image of mongoDB
- 🌐 Build a simple web app that use a API for TMDB to download the posters

## Features

- Take a poster movie
- Database for posters that you ask
- Full control of the DataBase (CRUD)


## Technologies
- 🌟 Bash-scripting
- ⭐ Python 
- 💫 Docker
- ⌛  Docker-compose
- 🗺️ Flask
- 💻 OOP
- 📱  Web API (TMDB)
- 🕹️ Mongodb
- 📟 Git

## requirements

- 📱  API key for imdb (Steps to make a new one in workflow)
- 🗺️ Docker
- 📟 Code editor

## WorkFlow
- 👨‍💻 Clone this project to your local PC (git clone https://github.com/jabbourdan/TMDB-project.git)


- 🚀 after cloning you need to have a TMDB API you can follow the stepts below:
        

        1. Go to https://www.themoviedb.org/ and create new account
        2. Go to settings and click on API
        3. Generate new API V3  
        
- 📱 Open the project that you clone in step 1 

        make new file with name config.py and copy in the API key that you genrate in step 2


- 💫 Install docker to your computer and go to the project that you clone then open a terminal (After you added the config file) :

        docker-compsoe -f docker-compose.yml up

- 💽 After few seconds will you see the IP link that you can access the code with it (like the photo below)



![Capture](https://user-images.githubusercontent.com/111487226/205933927-c6b007b8-448b-4ef1-b5a3-e60d4cffeb49.PNG)

- 👨‍💻 You will see this page you can choise if you want to search for a new posters ,delete a poster in data base that you searched for and update a photo name in database

![Screenshot 2022-12-06 003131](https://user-images.githubusercontent.com/111487226/205934544-949813e7-a366-43e6-9e98-ea4f5a2c7178.png)

note : sometimes the search_movie function line () dont work its a function in imdb libary that you can get a move name and ID . Example of output after searching for a movie :

![example](https://user-images.githubusercontent.com/111487226/205935388-0967c726-e2e2-4d68-8fb3-b53ff7c086a7.png)
