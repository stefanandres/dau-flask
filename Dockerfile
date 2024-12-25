FROM python:3.11-slim@sha256:873952659a04188d2a62d5f7e30fd673d2559432a847a8ad5fcaf9cbd085e9ed

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
