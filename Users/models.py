from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'



