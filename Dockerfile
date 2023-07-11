# This Dockerfile is for local development with Docker compose.
# It only copies and installs Python requirements, source code is mounted in docker-compose.yaml file.
FROM python:3.11

WORKDIR /usr/local/src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
