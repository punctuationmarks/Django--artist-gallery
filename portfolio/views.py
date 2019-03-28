from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView)
from .models import PortfolioPost




def portfolio(request):
    context = {
        'posts': PortfolioPost.objects.all()
    }
    return render(request, 'portfolio/portfolio.html', context, {'title':'Portfolio'})


class PostListView(ListView):
    model = PortfolioPost
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 12

class PostDetailView(DetailView):
    model = PortfolioPost



class PostCreateView(LoginRequiredMixin, CreateView):
    model = PortfolioPost
    fields = ['title', 'body', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PortfolioPost
    fields = ['title', 'body', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = PortfolioPost
    success_url = '/portfolio'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
