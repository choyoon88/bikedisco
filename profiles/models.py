from django.db import models
from django.contrib.auth.models import User
from review.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=50, blank=True, default='First Name')
    lastname = models.CharField(max_length=50, blank=True, default='Last Name')
    email = models.EmailField()
    reviewed = models.ManyToManyField(Post, related_name='reviewed', blank=True)

    def __str__(self):
        return str(self.user)