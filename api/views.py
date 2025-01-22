from django.shortcuts import render
from blog.models import Post
from .serializers import PostSerializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView



class PostApi(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class CreatPostApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class Unversal(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers