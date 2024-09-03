from django.db import models
from django.utils.timezone import now

class Project(models.Model):
    user_id = models.IntegerField(default=0)
    title = models.TextField(default="", max_length=50, blank=False)
    brief = models.TextField(default="", max_length=50, blank=False)
    goto_url = models.TextField(default="", max_length=200, blank=False)
    createtime = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['createtime']