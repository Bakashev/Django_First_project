from .models import Post
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, SingleObjectMixin
from django.urls import reverse_lazy

class Home(View):
    def get(self):
        return render(self.request, 'home_new.html')
class PostsList(ListView):
    model = Post
    template_name = 'home_new.html'


class ShowPost(DetailView):
    model = Post
    template_name = 'show_post_new.html'


class CreatPost(CreateView):
    model = Post
    template_name = 'create_post_new.html'
    fields = '__all__'

class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post_new.html'
    fields = ['title', 'content']



class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    queryset = None



