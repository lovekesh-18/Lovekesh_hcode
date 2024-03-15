from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # path('',profile,name="profile")
    path('',UploadFileClass.as_view(),name="profile"),
    path('list/',ProfileView.as_view(),name="profile_view")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)