from django.contrib import admin

# Register your models here.
from .models import HomePagePost, BioPagePost

admin.site.register(HomePagePost)
admin.site.register(BioPagePost)
