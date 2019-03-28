from django import forms
from .models import GalleryPost

class GalleryPostForm(forms.ModelForm):
    class Meta:
        model = GalleryPost
        fields = ['image']
