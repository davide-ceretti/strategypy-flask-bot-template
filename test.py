"""
NOTE: These tests require the application to be running
"""

import time
import json
from websocket import create_connection


some_ctx = {
    'grid_size': (40, 40),
    'has_killed': [],
    'respawn': False,
    'was_killed_by': [],
    'current_data': {
        0: {
            0: (10, 9),
            1: (19, 2),
            2: (0, 14),
            3: (5, 19),
            4: (16, 4),
            5: (9, 15),
            6: (26, 36),
            7: (16, 38),
            8: (10, 38),
            9: (31, 20)},
        1: {
            0: (3, 25),
            1: (17, 5),
            2: (7, 20),
            3: (9, 36),
            4: (3, 17),
            5: (22, 15),
            6: (10, 31),
            7: (23, 22),
            8: (23, 1),
            9: (31, 30)}
    },
    'pk': 2,
    'player_pk': 0,
    'position': (0, 14),
}


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed


def send_msg(ws):
    ws.send(json.dumps(some_ctx))
    result = ws.recv()
    print result


@timeit
def send_msgs(number):
    ws = create_connection("ws://localhost:8000")
    for _ in xrange(number):
        send_msg(ws)
    ws.close()


send_msgs(150)
