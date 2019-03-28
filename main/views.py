from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, UpdateView
from .models import BioPagePost, HomePagePost




def homePage(request):
    # rendering only the newest HomePagePost so it's the "updated" post
    # while also keeping all of the previous iterations
    context = {
        'post': HomePagePost.objects.last()
    }
    return render(request, 'main/home.html', context, {'title':'Home'})



def bioPage(request):
    context = {
        'post': BioPagePost.objects.last()
    }
    return render(request, 'main/bio.html', context, {'title':'Bio'})



class HomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = HomePagePost
    fields = ['title', 'body', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BioPagePost
    fields = ['title', 'body', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
