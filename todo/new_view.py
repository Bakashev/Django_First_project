
import datetime

from .models import Post, Comments
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, SingleObjectMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Max
from .forms import PostForm, UserForm
from user.models import User
class Home(View):

    def get(self, request):
        qs = Post.objects.all()
        return render(self.request, 'start_page.html', {'posts': qs})
class PostsList(ListView):
    model = Post
    template_name = 'home_new.html'
    paginate_by = 10
    # @staticmethod
    # def get_queryset():
    #     return Post.objects.all().select_related('user').values('title', 'created', 'user__username')



class ShowPost(DetailView):
    model = Post
    template_name = 'show_post_new.html'

@method_decorator(login_required, name='dispatch')

# Создание с использованием CreqateView
class CreatPost(CreateView):
    model = Post
    # template_name = 'create_post_new.html'
    # fields = ["title", "content"]


    def get(self, request):
        return render(request, 'create_post_new.html', {'form': PostForm})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        print(request.POST.getlist('title'))
        print(request.POST.getlist('content'))
        print(request.user)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            post = self.model.objects.create(
                title=title,
                content=content,
                user=request.user
            )

            post.save()
            return redirect(reverse('show_post', kwargs={'pk': post.id}))


# Создание с использованием View
# class CreatPost(View):
#
#     def get(self, request):
#         return render(request, 'create_post_new.html')
#     def post(self, request):
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         user_id = self.request.user.id
#         post = Post(title=title, content=content, user_id=user_id )
#         post.save()
#         return redirect(reverse('home' ))


# @method_decorator(login_required, name='dispatch')
class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    pk_url_kwarg = 'pk'
    template_name = 'edit_post_new.html'




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
    template_name = 'statistic.html'
    context_object_name = 'comments'


    def get_queryset(self):
        return Comments.objects.select_related('post')\
                        .filter(created__gte = (datetime.datetime.now() - datetime.timedelta(hours=12)))\
                        .values('post_id', 'post__title')\
                        .annotate(Count('post_id'))\
                        .order_by('-post_id__count')\
                        .filter(post_id__count__gt = 2)




class ShowComments(ListView):
    model = Comments
    template_name = 'show_comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comments.objects.all()\
                            .select_related('post').\
                            filter(created__gte = (datetime.datetime.now() - datetime.timedelta(hours=1200)))\
                            .values('post_id')\
                            .annotate(Count('post_id')).order_by('-post_id__count')\
                            .filter(post_id__count__gt = 2)\


class CreateComent(View):


    # def get(self, request):
    #     return render(request,'show_post.html', {'pk': "post.id"})


    def post(self, request, pk):

        post = get_object_or_404(Post, id=pk)
        conten = request.POST.get('coment')
        username = request.user
        useremail = request.POST.get('email')
        Comments.objects.create(username=username, conten=conten, useremail=useremail, post_id=post.id)

        return redirect(reverse('show_post', kwargs={'pk': post.id}))


class UserEdit(UpdateView):
    model = User
    form_class = UserForm
    pk_url_kwarg = 'pk'
    template_name = 'user_info.html'








