FROM python:3.9.5-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get -y install libjpeg-dev zlib1g-dev gcc
COPY ./backend .

RUN python -m pip install -U --force-reinstall pip
RUN pip install -r requirements.txt

COPY ../docker/backend-start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x ./start.sh
