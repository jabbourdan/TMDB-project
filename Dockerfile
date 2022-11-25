# Step 1 select default OS image
FROM alpine

# Step 2 Setting up environment
RUN apk update
RUN apk add --no-cache python3-dev && apk add py3-pip
RUN pip3 install --upgrade pip


# Step 3 Configure a software
WORKDIR /app

# Installing dependencies.
RUN pip3 install IMDbPY
RUN pip3 install requests
RUN pip3 install pymongo
RUN pip3 install flask
# RUN pip3 install -r requirements.txt 

# Copying project files.
COPY app.py /app
COPY download.py /app
COPY mongoDB.py /app
COPY config.py /app


RUN mkdir -p /app/templates
RUN mkdir -p /app/temp_content
COPY ./Templates/*  /app/templates




# Exposing an internal port
EXPOSE 5001


# Step 4 set default commands
ENTRYPOINT [ "python3" ]

# These commands will be replaced if user provides any command by himself
CMD [ "app.py" ]
