from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100) # по умолчанию null равен false обязательно для заполнения, хотим изменить изменить null=true
    created = models.DateField(auto_now_add=True) # автоматически создает время и не изменяемо,
    content = models.TextField()
    user =models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('show_post', args=[str(self.id)])

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=256)
    useremail = models.EmailField()
    conten = models.TextField()
    created = models.DateTimeField(auto_now_add=True)





