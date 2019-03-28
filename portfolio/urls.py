from django.urls import path
from . import views

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)

urlpatterns = [
    path('', PostListView.as_view(), name='portfolio'),
    path('portfolio_post/<int:pk>/', PostDetailView.as_view(), name='portfolio-post-detail'),
    path('portfolio_post/new/', PostCreateView.as_view(), name='portfolio-post-create'),
    path('portfolio_post/<int:pk>/update', PostUpdateView.as_view(), name='portfolio-post-update'),
    path('portfolio_post/<int:pk>/delete', PostDeleteView.as_view(), name='portfolio-post-delete')

]
