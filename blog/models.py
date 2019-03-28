from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    # date that can be updated
    date_posted = models.DateTimeField(default=timezone.now)
    # this will update the time, every time a post is updated
    last_modified = models.DateTimeField(auto_now=True)
    # sets the datetime only to when the post is originally created,
    # you can never update the date posted argument
    date_original_posted = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # this is done so that once a post is created, the user
    # is redirected directly to that detailed view
    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'pk':self.pk})
