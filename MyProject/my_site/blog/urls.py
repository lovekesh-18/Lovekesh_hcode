from django.urls import path
from .views import *

urlpatterns = [
    path('',starting_page,name="starting-page"),
    path('post',posts,name="posts-page"),
    path('post/<slug:slug>',post_detail,name="post-detail-page")
]


