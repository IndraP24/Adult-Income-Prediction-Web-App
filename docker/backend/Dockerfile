FROM ubuntu:focal

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.8 python3.8-dev python3-pip

WORKDIR /app
COPY requirements.txt .
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.8 /usr/bin/python
RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.8 /usr/bin/python3

RUN pip install -r requirements.txt
RUN pip install gunicorn

ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./artifacts /app/artifacts

RUN mkdir -p /app/backend/server/static