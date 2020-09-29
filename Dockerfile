FROM python:3.8.0
ENV PYTHONUNBUFFERED=1
RUN mkdir /backend-django-taskmanager
WORKDIR /backend-django-taskmanager
COPY requirements.txt /backend-django-taskmanager/
RUN pip install -r requirements.txt
COPY . /backend-django-taskmanager/