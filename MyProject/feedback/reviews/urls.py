from django.urls import path
from .views import *

urlpatterns = [
    path('',ReviewView.as_view(),name="index"),
    path('show',show,name="show_time")
]