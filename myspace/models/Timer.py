from django.db import models
from django.utils.timezone import now

class Timer(models.Model):
    tid = models.IntegerField(default=0)
    TimeStamp = models.DateTimeField(default=now) 

class Answer(models.Model):
    user_id = models.IntegerField()
    TimeStamp = models.DateTimeField()

    def __str__(self):
        return str(self.user_id) 
    
    class Meta: 
        ordering=['TimeStamp']