FROM ubuntu:18.04

LABEL maintainer="mjee245@gmail.com"
LABEL version="0.1"
LABEL description="Docker image for tickets server"

RUN apt update && apt install -y python3 python3-pip mysql-client libmysqlclient-dev && mkdir /tmp/TicketServer


COPY . /srv/TicketServer/

RUN cd /srv/TicketServer/ && pip3 install -r requirements.txt

CMD ["RUN", "python3", "manage.py", "collectstatic", "--noinput"]
CMD ["python3", "/srv/TicketServer/manage.py", "runserver"]
