from datetime import datetime

from .models import Post, Comments
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, SingleObjectMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Max
class Home(View):

    def get(self, request):
        qs = Post.objects.all()
        return render(self.request, 'start_page.html', {'posts': qs})
class PostsList(ListView):
    model = Post
    template_name = 'home_new.html'
    # @staticmethod
    # def get_queryset():
    #     return Post.objects.all().select_related('user').values('title', 'created', 'user__username')



class ShowPost(DetailView):
    model = Post
    template_name = 'show_post_new.html'

#@method_decorator(login_required, name='dispatch')
class CreatPost(CreateView):
    model = Post
    template_name = 'create_post_new.html'
    fields = '__all__'
    # def post (self, id):
    #     post = Post.objects.create(
    #         title='title',
    #         content='content',
    #         created=datetime.now(),
    #         user_id=id)
@method_decorator(login_required, name='dispatch')
class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post_new.html'
    fields = ['title', 'content']



@method_decorator(login_required, name='dispatch')
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    queryset = None

    def has_object_permision(self, post: Post):
        return post.user.id == self.request.user.id


class UserList(ListView):
    model = Post
    template_name = 'users.html'
    context_object_name = 'users'
    @staticmethod
    def get_queryset():

        return Post.objects.all().select_related('user')\
                            .values('user__username', 'user_id')\
                            .annotate(Count('user_id'))\
                             .annotate(Max('created'))\
                            .order_by("-user_id__count")

class StatisticComents(ListView):
    model = Comments
    template_name = 'show_comments.html'
    context_object_name = 'commments'

    @staticmethod
    def get_queryset():

        return Comments.objects.all()\
                            .select_related('post').\
                            filter(created__gte = (datetime.datetime.now() - datetime.timedelta(hours=12)))\
                            .values('post_id')\
                            .annotate(Count('post_id')).order_by('-post_id__count')\
                            .filter(post_id__count__gt = 2)\

class CreateComent(CreateView):
    model = Comments
    template_name = 'create_comments.html'
    fields = '__all__'







