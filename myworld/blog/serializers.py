#-*-coding:utf-8-*-
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name',)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name',)



class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer()
    class Meta:
        model = Post
        fields = ('id','title','body','created_time','category','tags','author','views')
        read_only_fields = ('id','created_time',)