from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.utils.timezone import now
from datetime import timedelta


_MAX_SIZE = 150


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='аватар')
    age = models.PositiveIntegerField(verbose_name='возраст')
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

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

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        return True

