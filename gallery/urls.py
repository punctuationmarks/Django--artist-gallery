from django.urls import path
from . import views

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)

urlpatterns = [
    path('', PostListView.as_view(), name='gallery'),
    path('gallery_post/<int:pk>/', PostDetailView.as_view(), name='gallery-post-detail'),
    path('gallery_post/new/', PostCreateView.as_view(), name='gallery-post-create'),
    path('gallery_post/<int:pk>/update', PostUpdateView.as_view(), name='gallery-post-update'),
    path('gallery_post/<int:pk>/delete', PostDeleteView.as_view(), name='gallery-post-delete')

]
