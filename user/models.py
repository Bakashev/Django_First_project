from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=256, null=True)
    avatar = models.ImageField(upload_to='image', default=None, null=True)

    class Meta:
        db_table = 'user'

    def get_absolute_url(self):
        return reverse('home')

    @property
    def photo_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url