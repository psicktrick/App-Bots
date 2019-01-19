from __future__ import absolute_import
from celery import Celery

app = Celery('src',
             broker='amqp://saurabh:saurabh123@localhost/saurabh1_vhost',
             backend='redis://localhost',
             include=['src.tasks'])


