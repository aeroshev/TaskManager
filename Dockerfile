FROM python:3.8.0

ENV PYTHONUNBUFFERED=1

RUN pip3 install pipenv

RUN mkdir /code
WORKDIR /code

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

COPY . .

EXPOSE 8000
