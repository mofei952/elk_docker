import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/api/hit')
def hit():
    count = cache.incr('hit_count')
    return 'Hello World! I have been seen {} times.\n'.format(count)
