from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('',starting_page,name="starting-page"),
    path('',StartPage.as_view(),name="starting-page"),
    # path('post',posts,name="posts-page"),
    path('post',All_Post.as_view(),name="posts-page"),
    # path('post/<slug:slug>',post_detail,name="post-detail-page")
    path('post/<slug:slug>',Post_Detail.as_view(),name="post-detail-page"),
    path('readlater/',ReadLaterView.as_view(),name="read-later")
]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


