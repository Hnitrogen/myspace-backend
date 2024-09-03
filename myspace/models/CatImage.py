from django.db import models
from django.contrib.auth.models import User

class CatImage(models.Model): 
    name = models.CharField(max_length=200),
    created = models.DateTimeField(auto_now_add=True) 
    picture = models.ImageField(upload_to='img/',verbose_name=u"image_location")

    def __str__(self):
        return str(self.picture)[4:]
    
    class Meta: 
        ordering=['created']