from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('<int:month>',all_function_number),
    path('<str:month>',all_function,name="month-url-name")
]