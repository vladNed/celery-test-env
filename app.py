from tasks import add
from celery import group, signature
from celery.result import states
import time

result = group([
    signature(
        'tasks.add',
        kwargs={
            'volume': 645,
            'data': 10
        },
        immutable=True
    ),
    signature(
        'tasks.add',
        kwargs={
            'volume': 785,
            'data': 2
        },
        immutable=True
    )
])
async_stuff = result.apply_async()
state = [i.state == states.PENDING for i in async_stuff.results]
while any(state):
    time.sleep(2)
    print('..wating')
    state = [i.state == states.PENDING for i in async_stuff.results]


print(async_stuff.get())