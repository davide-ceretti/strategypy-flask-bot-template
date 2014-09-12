FROM ubuntu:12.04
RUN apt-get update
RUN apt-get install -y python-setuptools libevent-dev gcc python-dev
RUN easy_install pip
RUN pip install flask-sockets

ADD bot.py /code/work/bot.py

VOLUME /code/work

WORKDIR /code/work

EXPOSE 8000

CMD python bot.py
