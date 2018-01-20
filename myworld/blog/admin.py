from django.contrib import admin

# Register your models here.
from .models import *
from  django.contrib.auth.models import User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]

admin.site.register(Category, CategoryAdmin)




class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]

admin.site.register(Tag, TagAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','body','created_time','category','author','views',]

admin.site.register(Post, PostAdmin)
