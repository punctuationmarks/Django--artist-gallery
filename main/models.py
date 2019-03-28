from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class HomePagePost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(default="default.jpg", upload_to='home_pics')

    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, { self.body}'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

class BioPagePost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(default="default.jpg", upload_to='bio_pics')

    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, { self.body}'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
