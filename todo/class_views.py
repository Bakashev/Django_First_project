from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.urls import reverse
from django.http import HttpResponseNotAllowed
from django.views import View, generic


class PostsList(View):

    @staticmethod
    def get_qureset():
        return Post.objects.all()

    def get(self, request):
        posts = self.get_qureset()
        return render(request,'home.html', {'posts': posts})


class NotNumbersPostsList(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'posts'
    # Заменяем на get_quareset()
    #queryset = Post.objects.filter(title__iregex=r'^\D+$').all()
    def validate(self):
        s = self.request.GET.get('search')
        return s is not None and len(s) <= 50

    def get_queryset(self):
        if not self.validate():
            return Post.objects.all()
        search = self.request.GET['search']
        print(self.request.GET)
        return  Post.objects.filter(title__icontains=search)

    # для работы если бы мы наследовались не из generic.ListView а от PostsListзнерщт
    # @staticmethod
    # def get_qureset():
    #     return Post.objects.filter(title__iregex=r'^\D+$').all()

class PostValidate:
    #@staticmethod
    def is_valid(self, title: str, content: str) -> bool:
        return self.title_valid(title) and self.content_valid(content)

    def title_valid(self, title: str) ->bool:
        if not bool(title):
            return False
        else:
            return len(title) <=300

    def content_valid(self, content:str) -> bool:
        if not bool(content):
            return False
        else:
            return len(content) < 30_000

class CreatPost(View, PostValidate):

    def get(self, request):
        return render(request,'create_post.html')


    def post(self, request):
        title = request.POST.get('zagolovok')
        content = request.POST.get('soderjimoe')
        errors = []

        if not self.is_valid(title, content):
            errors.append('Заполнить')
            return render(request, 'create_post.html', {'errors': errors})

        post = Post(title=title, content=content)
        post.save()
        return redirect(reverse('show_post', kwargs={'post_id': post.id}))