from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100) # по умолчанию null равен false обязательно для заполнения, хотим изменить изменить null=true
    created = models.DateField(auto_now_add=True) # автоматически создает время и не изменяемо,
    content = models.TextField()


