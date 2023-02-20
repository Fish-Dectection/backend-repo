from .celery import app
from .model import Caught_fish
import requests

@app.task
def decision(response):
    
    ai_url = 'http://localhost:5001/model'
    fish = response.objects.get()

    requests.post(ai_url,json={"id":response})

    json_list = []    

    json_list.append({
        "main_fish_id" : fish.main_fish_id,
        "main_fish_accuracy" : main_fish_accuracy,
        "sub1_fish_id" : sub1_fish_id,
        "sub1_fish_accuracy" : sub1_fish_accuracy,
        "sub2_fish_id" : sub2_fish_id,
        "sub2_fish_accuracy" : sub2_fish_accuracy
    })

    return json_list


