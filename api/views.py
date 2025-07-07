from django.shortcuts import render
from . import serializers, models
from rest_framework import generics


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer
    lookup_field = "pk"


