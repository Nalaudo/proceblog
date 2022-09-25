from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    img = models.ImageField(upload_to='postImg', null=True, blank=False)
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200)
    body = RichTextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse('postDetail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='avatar', null=True, blank=True)


class Contact(models.Model):
    user = models.CharField(max_length=250)
    message = RichTextField()

    def __str__(self):
        return self.user
