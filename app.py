import time

import reddis
from flask import Flask

app = Flask(__name__)
cache = redis.Reddis(host='reddis', port=8080)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello sahithi'
