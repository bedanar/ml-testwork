FROM python:3

WORKDIR /usr/src/app

COPY . ./
RUN pip install -r requirements.txt

RUN apt-get update 
RUN apt-get install tar

COPY data.tgz data.tgz

RUN tar zxfv data.tgz


