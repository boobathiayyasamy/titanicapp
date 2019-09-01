FROM ubuntu:latest

MAINTAINER Boobathi Ayyasamy  "boobathi.ayyasamy@gmail.com"

#RUN apt-get update -y

#RUN apt-get install -y python3-pip python3-dev build-essential

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev build-essential \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

#FROM python:3

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]
