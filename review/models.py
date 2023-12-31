from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Post model basic structure is from CI's walkthrough session
    but it has custom added fields that is related with CityBike API
    Model for posting a review
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    station_name = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = slug
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    comment model is associated with each post from Post model
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='commentsuser',
        null=True
        )
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return f"Comment by {self.user}"
