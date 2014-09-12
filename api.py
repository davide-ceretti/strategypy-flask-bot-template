import json

from flask import Flask
from flask_sockets import Sockets

from bot import get_action

app = Flask(__name__)
app.debug = True
sockets = Sockets(app)


@sockets.route('/')
def echo_socket(ws):
    while True:
        message = ws.receive()
        if message is not None:
            ws.send(get_action(json.loads(message)))
        else:
            break
