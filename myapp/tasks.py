from celery import shared_task
@shared_task
def hello_world():
    print("Hello, World! Celery Beat and Worker are running successfully.")
    return "done"
