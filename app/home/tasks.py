import logging
import time
from celery.decorators import task

logger = logging.getLogger('celery')


@task(name='test_task_one')
def test_task_one(value):
    logger.info('test_task_one: executed')
    logger.info('Starting sleep for: {}'.format(value))
    time.sleep(30)
    return '30 second sleep done for: {}'.format(value)


@task(name='test_task_two')
def test_task_two():
    logger.info('test_task_one: executed')
    logger.info('Starting sleep for 30 seconds')
    time.sleep(30)
    return '30 second sleep done'
