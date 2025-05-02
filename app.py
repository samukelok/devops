from flask import Flask
import redis
import os

app = Flask(__name__)
cache = redis.Redis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=6379,
    decode_responses=True
)

@app.route('/')
def home():
    return "Welcome to the DevOps Flask API! Use /visits endpoint"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)