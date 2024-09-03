from django.db import models
from django.utils.timezone import now
from taggit.managers import TaggableManager


class Post(models.Model):
    user_id = models.IntegerField(default=0)
    title = models.TextField(default="", max_length=50, blank=False)
    content = models.TextField(default="", max_length=1000000, blank=True, null=True)
    createtime = models.DateTimeField(default=now)
    pic_url = models.TextField(default="", max_length=100,
                               blank=False)

    # taggit
    tags = TaggableManager()

    def __str__(self):
        return str(self.user_id) + ' - ' + self.title

    class Meta:
        ordering = ['-createtime']  # 逆序前面加-号


class PostComment(models.Model):
    author = models.TextField(max_length=50, blank=False)
    attach_id = models.IntegerField(default=0)
    createtime = models.DateTimeField(default=now)
    content = models.TextField(max_length=1000, blank=False)
    content_location = models.TextField(max_length=50, blank=False)

    def __str__(self):
        return str(self.attach_id) + "  " + self.author

    class Meta:
        ordering = ['-createtime']
