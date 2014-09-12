FROM ubuntu:12.04
RUN apt-get update
RUN apt-get install -y python-setuptools libevent-dev gcc python-dev
RUN easy_install pip
RUN pip install flask-sockets
RUN pip install gunicorn

ADD bot.py /code/work/bot.py

VOLUME /code/work

WORKDIR /code/work

EXPOSE 8000

CMD gunicorn -k flask_sockets.worker -b 0.0.0.0:8000 api:app
