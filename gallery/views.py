from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView)


from .models import GalleryPost




def gallery(request):
    context = {
        'posts': GalleryPost.objects.all()
    }
    return render(request, 'gallery/gallery.html', context, {'title':'Portfolio'})



class PostListView(ListView):
    model = GalleryPost
    template_name = 'gallery/gallery.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 12

class PostDetailView(DetailView):
    model = GalleryPost



class PostCreateView(LoginRequiredMixin, CreateView):
    model = GalleryPost
    fields = ['title', 'body', 'image', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = GalleryPost
    fields = ['title', 'body', 'image', 'price']

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = GalleryPost
    success_url = '/gallery'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
