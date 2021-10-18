# pull official base image
FROM python:3.7.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

RUN pip install --upgrade pip && apk add --virtual build-deps gcc python-dev musl-dev && apk add postgresql-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .