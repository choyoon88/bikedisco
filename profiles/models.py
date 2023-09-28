from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from review.models import Post
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    """
    Profile class for creating a profile for
    the user that is associated with the User model
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    firstname = models.CharField(
        max_length=50,
        blank=True,
        default='Enter your first name'
        )
    lastname = models.CharField(
        max_length=50,
        blank=True,
        default='Enter your last name'
        )
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return str(self.user)


def create_profile(sender, instance, created, **kwargs):
    """
    when the user joins the website
    it instantly creates a profile
    that is associated with the User model
    """
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.email = instance.email
        user_profile.save()


post_save.connect(create_profile, sender=User)
