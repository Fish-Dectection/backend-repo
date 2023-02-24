from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .celery import app
#from .model import Caught_fish
import requests

@shared_task
def decision(response):
    
    # ai_url = 'http://localhost:5001/model'
    # fish = response.objects.get()

    test = requests.post('http://localhost:5001/test/',json={"id": response.data}) 
    print(test)    

    #requests.post(ai_url,json={"id":response})
    return test


