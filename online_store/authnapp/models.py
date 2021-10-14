from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


_MAX_SIZE = 150


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='аватар')
    age = models.PositiveIntegerField(verbose_name='возраст')

    def save(self, *args, **kwargs):
        super(ShopUser, self).save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > _MAX_SIZE or img.width > _MAX_SIZE:
                img = img.resize(
                    (_MAX_SIZE, _MAX_SIZE),
                    Image.ANTIALIAS
                )
                img.save(self.avatar.path)
