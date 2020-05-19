from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# function based view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based view for home
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # by default, the view will look in <app>/<model>_<viewtype>
    context_object_name = 'posts' # overwriting the name of the list. otherwise it would be object_list
    ordering = ['-date_posted'] # order the query the minus sign reverses the default ordering (default is oldest to newest)

class PostDetailView(DetailView):
    model = Post

# mixin to redirect to login screen if not logged in
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # the default template will be post_form.html
    # must specify the fields you want
    fields = ['title', 'content']

    # overwriting the valid method to add the user that is logged in to the form, then validating that new form
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # if wanted, could set a success_url and it will redirect there instead of 

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # the default template will be post_form.html
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this method is ran because of the UserPassesTestMixin. we use to check for user editing its own post
    def test_func(self):
        # gets the post we are trying to update
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # default tempalte name is post_confirm_delete.html where the submit button confirms the deletion
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })