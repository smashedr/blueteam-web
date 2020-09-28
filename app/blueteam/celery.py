import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blueteam.settings')

app = Celery('blueteam')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-60-seconds': {
        'task': 'test_task_two',
        'schedule': crontab('*/1')
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
