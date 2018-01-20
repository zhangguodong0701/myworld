#-*-coding:utf-8-*-
from django.conf.urls import url,include
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns



app_name = 'blog'
urlpatterns = [
    url(r'^post_list/$', views.PostListView.as_view(), name='post_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)