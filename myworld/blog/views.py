from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics,permissions
from .models import Post
from .serializers import PostListSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination




class PostListView(generics.ListCreateAPIView):
    """
    产品列表
    """
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('created_time')
    search_fields = ('body', 'title',)
    ordering = ('id',)
    pagination_class = LimitOffsetPagination
