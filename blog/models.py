from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categorys", args={self.slug})


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')



class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='rasmlar/')
    description = models.TextField()
    create_ad = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft',
    blank=True, null=True)
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title