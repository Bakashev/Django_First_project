from django.forms import ModelForm
from .models import Post
from user.models import User

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title",  "content"]



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username",  "address", 'avatar', 'email', 'last_name']



