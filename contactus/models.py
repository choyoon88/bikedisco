from django.db import models


class Contact(models.Model):
    """
    Contact model is used for each
    contact submitted by the site user
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return str(self.name)
