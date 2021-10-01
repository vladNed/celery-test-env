from typing import Tuple
from celery import Celery
import random

app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')


def success_code(self, retval, task_id, args, kwargs):
    result, send_notification = retval
    print(f"> ON_SUCCESS: ret:{retval}, id: {task_id}, args:{args}, kwargs: {kwargs}")

    print(f"THE RESULT WAS: {result}")
    if send_notification:
        print("BING!!!! NOTIFICATION")

def fail_code(self, exc, task_id, args, kwargs, einfo):
    print(f"> FAILURE: exc:{exc}, kwargs: {kwargs}")

    print(kwargs.get('section'))

@app.task(
    bind=True,
    default_retry_delay=1,
    max_retries=10,
    on_success=success_code,
    on_failure=fail_code
)
def generate_password(self, section: int, name: int) -> Tuple[bool, bool]:
    password_hash = hash(f"OS-{name}-{section}-{random.randint(100,500)}")
    if password_hash % 10 < 500:
        print(f":( -> {password_hash % 10}")
        raise self.retry()


    return True, True



