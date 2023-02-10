from django.db import models
from django.utils import timezone
from django.models import Fish

# Create your models here.
class Caught_fish(models.Model):
    fish_length = models.FloatField()
    user_region = models.CharField(max_length=225)
    image_url = models.CharField(max_length=225)

    main_fish_id = models.ForeignKey(Fish, on_delete=models.CASECADE)
    main_fish_accuracy = models.FloatField()
    sub1_fish_id = models.ForeignKey(Fish, on_delete=models.CASECADE)
    sub1_fish_accuracy = models.FloatField()
    sub2_fish_id = models.ForeignKey(Fish, on_delete=models.CASECADE)
    sub2_fish_accuracy = models.FloatField()
    
    create_at = models.DataTimeField(default=timezone.now)
    update_at = models.DataTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)



    