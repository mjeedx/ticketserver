FROM ubuntu:18.04

LABEL maintainer="mjee245@gmail.com"
LABEL version="0.1"
LABEL description="Docker image for tickets server"

RUN apt update && apt install -y python3 python3-pip mysql-client libmysqlclient-dev && mkdir /tmp/TicketServer


COPY . /srv/TicketServer/

