from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='rasmlar/')
    description = models.TextField()
    create_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title