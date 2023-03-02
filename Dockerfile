# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && apt-get update && apt-get install -y iputils-ping

COPY . /app

EXPOSE 8080
CMD ["python3", "app.py"]