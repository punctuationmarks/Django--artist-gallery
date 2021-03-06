from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class PortfolioPost(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(default="default.jpg", upload_to='portfolio_pics')


    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, { self.image}'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('portfolio-post-detail', kwargs={'pk':self.pk})
