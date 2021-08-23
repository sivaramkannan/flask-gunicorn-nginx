from flask import Flask, request
import json
import logging, sys

app = Flask(__name__)


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/wait')
def wait():
    from random import randint
    from time import sleep
    waittime = randint(10,15)
    logging.info('Going to sleep for some random seconds!')
    sleep(waittime)
    logging.info('Just woke up')
    return str(waittime)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
