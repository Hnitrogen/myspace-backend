from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='docs/')

    def __str__(self):
        return self.title
    