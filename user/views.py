from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from .forms import UserForm
class UserEdit(UpdateView):
    model = User
    form_class = UserForm
    pk_url_kwarg = 'pk'
    template_name = 'user_info.html'



