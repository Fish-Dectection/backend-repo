from celery import Celery
import os
from django import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('caught_fish',
            broker='',
            backend='',
            include=['caught_fish.tasks'])