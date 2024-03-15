from django.urls import path
from .views import *

urlpatterns = [
    path('',ReviewView.as_view(),name="index"),
    path('new',NewReviewView.as_view()),
    path('newnew',NewNewReviewView.as_view()),
    path('show',show,name="show_time"),
    path('review_all',ReviewListView.as_view()),
    path('template_base',TemplateBaseView.as_view()),
    path('single_review/<int:id>',SingleReviewView.as_view()),
    path('ReviewDetailView/<int:pk>',SingleReviewDetailView.as_view())
]