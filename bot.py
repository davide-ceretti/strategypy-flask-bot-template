import random


def get_action(ctx):
    actions = [
        'move up',
        'move left',
        'move right',
        'move down',
    ]

    return random.choice(actions)
