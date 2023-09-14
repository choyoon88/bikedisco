from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_posts")
    # bike_station_country = models.ForeignKey(BikeStationCountry, on_delete=models.CASCADE)
    # bike_station_city = models.ForeignKey(BikeStationCity, on_delete=models.CASCADE)
    # bike_station_name = models.ForeignKey(BikeStationName, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# class BikeStationCountry(models.Model):
#     name = models.CharField(max_length=250)

# class BikeStationCity(models.Model):
#     name = models.CharField(max_length=250)
#     country = models.ForeignKey(BikeStationCountry, on_delete=models.CASCADE)

# class BikeStationName(models.Model):
#     name = models.CharField(max_length=250)
#     city = models.ForeignKey(BikeStationCity, on_delete=models.CASCADE)