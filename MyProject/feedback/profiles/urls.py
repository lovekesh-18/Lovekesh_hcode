from django.urls import path
from .views import *
urlpatterns = [
    # path('',profile,name="profile")
    path('',UploadFileClass.as_view(),name="profile"),
    path('list/',ProfileView.as_view(),name="profile_view")
] 