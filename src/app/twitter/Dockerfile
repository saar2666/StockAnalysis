# pull official base image
FROM ubuntu 
RUN apt-get update
RUN apt-get -y install python3.9
RUN apt-get -y install python3-pip
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN set -eux \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip \
    && apt-get install -y git \
    && pip install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint

# copy project
COPY . /usr/src/app/