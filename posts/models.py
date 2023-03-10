from django.db import models
from django.urls import reverse
from django.conf import settings

def upload_path(instance, filename):
    return '/static/'.join([str(instance.title),filename])

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/')
    caption = models.TextField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " by " + str(self.author)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

