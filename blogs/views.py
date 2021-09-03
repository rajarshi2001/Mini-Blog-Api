from django.shortcuts import render
from .serializers import PostsSerializer
from rest_framework import viewsets
from .models import Posts

class postView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
