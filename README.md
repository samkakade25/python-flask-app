# python-flask-app

## Command to local setup

pip install flask
pip install concurrent-log-handler (concurent file rotation)

## To run latest version of app

chmod +x LATEST_TAG (execute latest version and build docker image of it)

## Docker File :

docker build -t pyhton-flask-app .
docker run -p 5000:5000 python-flask-app

command to execute commands inside container-
docker exec -it <container_id_or_name> /bin/bash

## To locally run the application :

1. Fork the repo
2. pull main branch
3. Run command - docker-compose up -d
4. And access endpoints on http://www.localhost & http://www.localhost/error

## Log collection strategy :

For Acesslogs we can collect every monday and zip the file to save storage space and if any condition file gets larger than 10MB we rotate the file and create newone.

For Errorlogs we can collect daily midnight(12 AM) and zip the file
