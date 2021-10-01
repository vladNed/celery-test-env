import tasks
import time

task = tasks.app.send_task(
    name="tasks.generate_password",
    kwargs={
        "section": 200,
        "name": "vladNed"
    }
)

count = 0
print("> START - Starting password generation")
while count < 10:
    if task.successful():
        print(f"> SUCCESS - result: {task.result}")
        break
    else:
        print(f"> WAIT - count: {count}")
        time.sleep(2)
        count += 1

if count >= 10:
    print("> FAILED !!!!!!!!")
