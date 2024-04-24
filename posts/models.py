from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/%y/%m/%d")
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slugs = models.SlugField(max_length=200, blank=True)
    date_posted = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="posts_liked", blank=True)
    
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.slugs:
            self.slugs = slugify(self.title)
        super().save(*args, **kwargs)
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    comment = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=100)
    date_commented = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ("date_commented",)
    
    def __str__(self):
        return self.comment