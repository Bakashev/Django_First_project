
from django.http import  HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.urls import reverse

def home(request):
    """
    Отображение всех полей на главной страницы.

    :param request: Всегда первый запрос от пользователя
    :return:
    """

    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def create_post(request):
    '''

    Создание новых заметок
    :param request:
    :return:
    '''
    errors = []
    if request.method == 'POST':
        title = request.POST.get('zagolovok')
        content = request.POST.get('soderjimoe')

        if not title or not content:
            errors.append('Укажите знаение')

        else:
            post = Post(title=title, content=content)
            post.save()

            return redirect(reverse('show_post', kwargs={'post_id': post.id}))

    return render(request, 'create_post.html', {'errors': errors})

def show_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return render(request,'show_post.html', {'post': post})


def edit_post(request, post_id: int):
    errors = []
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':

        title = request.POST.get('zagolovok')
        content = request.POST.get('opisanije')
        post.title = title
        post.content = content

        if not title or not content:
            errors.append('Укажите знаение')

        else:

            post.save()

            return  redirect(reverse('show_post', kwargs={'post_id': post_id}))


    return render(request, 'edit_post.html', {'errors': errors, 'post': post})


def post_delete(request, post_id: int):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        posts = Post.objects.all()
    else:
        return  HttpResponseNotAllowed(permitted_methods=['Post'])



    return render(request, 'home.html', {'posts': posts})

