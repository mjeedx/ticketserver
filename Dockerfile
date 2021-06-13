FROM ubuntu:18.04

LABEL maintainer="mjee245@gmail.com"
LABEL version="0.1"
LABEL description="Docker image for tickets server"
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y python3 python3-pip mysql-client libmysqlclient-dev && mkdir /tmp/ticketserver

COPY . /srv/ticketserver/

RUN cd /srv/ticketserver/ && pip3 install -r requirements.txt

RUN python3 /srv/ticketserver/manage.py collectstatic --noinput && python3 /srv/ticketserver/manage.py makemigrations && python3 /srv/ticketserver/manage.py migrate
CMD ["python3", "/srv/ticketserver/manage.py", "runserver", "0.0.0.0:8080"]
