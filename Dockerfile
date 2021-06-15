FROM ubuntu:18.04

LABEL maintainer="mjee245@gmail.com"
LABEL version="0.1"
LABEL description="Docker image for ticketserver"
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y python3 python3-pip mysql-client libmysqlclient-dev nginx && mkdir /srv/ticketserver

COPY . /srv/ticketserver/
WORKDIR /srv/ticketserver/

#RUN cp nginx/default.conf /etc/nginx/conf.d/default.conf && service nginx restart && \
RUN pip3 install -r requirements.txt && python3 manage.py collectstatic --noinput

RUN echo test

RUN python3 manage.py makemigrations && python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
