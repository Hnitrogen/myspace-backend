from django.db import models
from django.utils.timezone import now

class Paste(models.Model):
    user_id = models.IntegerField(default=0)
    title = models.TextField(default="None", max_length=50, blank=False)
    author = models.TextField(default="None",max_length=20,blank=True)
    content = models.TextField(default="", max_length=20000, blank=False)
    createtime = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['createtime']