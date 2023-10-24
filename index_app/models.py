from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(default='',max_length=20)
    comment = models.TextField(default='',max_length=1000)

    def __str__(self):
        return self.name