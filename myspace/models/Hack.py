from django.db import models
from django.utils.timezone import now

class HackerImage(models.Model):
    code_id = models.IntegerField(default=0) 
    created = models.DateTimeField(auto_now_add=True) 
    picture = models.ImageField(upload_to='hacker/',verbose_name=u"image_location")

    def __str__(self):
        return str(self.code_id) 

    class Meta: 
        ordering=['code_id']