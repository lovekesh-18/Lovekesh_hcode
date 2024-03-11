from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('<slug:slug>',detail_page,name="detail-page")
]