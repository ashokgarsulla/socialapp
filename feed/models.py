from django.db import models

# Create your models here.
class Post(models.Model):
    userid = models.IntegerField(default=1)
    caption = models.TextField(max_length=1000)
    attachment = models.FileField(upload_to= 'photovideos')
    likes = models.CharField(default=0,max_length=1000)

    def __str__(self):
        return self.caption