from celery import Celery
import time

app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')

DB = {}

@app.task
def add(volume: int, data: int):
    time.sleep(data)
    _hash = volume % 10
    if DB.get(_hash):
        DB[_hash] += 1
    else:
        DB[_hash] = 0
