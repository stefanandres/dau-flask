FROM python:3.11-slim@sha256:7e44de6fe87a9213c6ec7271a2b2c681ef2e8cd172fce65cc983f105a750efa0

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
