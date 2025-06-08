from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Posts(models.Model):
    title = models.CharField('Post title', max_length=100, null=False, blank=False)
    excerpt = models.CharField('Post excerpt', max_length=250, null=False, blank=False)
    body = models.TextField('Post body', null=False, blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return f'/forum/{self.id}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    post = models.ForeignKey('Posts', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"


class PostImage(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Image for Post {self.post.id}"

class Faq(models.Model):
    question = models.CharField(max_length = 400, blank=False)
    answer = models.TextField(max_length = 400, blank=False)

    def __str__(self):
        return self.question