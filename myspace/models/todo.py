from django.db import models
from django.utils.timezone import now

class TodoList(models.Model):
    LEVEL_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    title = models.CharField(max_length=50,null=False,blank=False,default='默认标题')
    content = models.TextField(default="", max_length=500, blank=True, null=True)
    createtime = models.DateTimeField(default=now)
    level = models.CharField(max_length=10,choices=LEVEL_CHOICES,default='low')
    percent = models.CharField(max_length=10,default='0%')

    def __str__(self):
        return str(self.content) 
    
    class Meta: 
        ordering = ['createtime']