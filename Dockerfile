FROM python:3.11-slim@sha256:ff0cf9465290d0d5949ae0bcc71c085d0b53d87246211522417e3cafa7da293b

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
