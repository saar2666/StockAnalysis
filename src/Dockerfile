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
    && pip install -r /usr/src/app/requirements.txt

# copy project
COPY . /usr/src/app/



# FROM ubuntu
# RUN apt-get update

# RUN apt-get -y install python3.9
# RUN apt-get -y install python3-pip
# RUN pip install httpx
# RUN pip install httpx
# RUN pip install FastAPI
# RUN pip install "uvicorn[standard]"
# RUN pip install nest-asyncio
# RUN pip install googletrans==3.1.0a0
# RUN pip install pytest


# WORKDIR /app

# COPY . .

# # Install software 
# RUN apt-get install -y git
# RUN pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint


# # CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "8080" ]

