from django.db import models
from django.utils import timezone
from fish.models import Fish

# Create your models here.
class Caught_fish(models.Model):
    fish_length = models.FloatField()
    user_region = models.CharField(max_length=225)
    image_url = models.CharField(max_length=225)

    main_fish_id = models.ForeignKey(Fish, on_delete=models.CASECADE, null=True)
    main_fish_accuracy = models.FloatField(null=True)
    sub1_fish_id = models.ForeignKey(Fish, on_delete=models.CASECADE, null=True)
    sub1_fish_accuracy = models.FloatField(null=True)
    sub2_fish_id = models.ForeignKey(Fish, on_delete=models.CASECADE, null=True)
    sub2_fish_accuracy = models.FloatField(null=True)
    
    create_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)


    