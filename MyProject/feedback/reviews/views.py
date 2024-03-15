from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView,CreateView
# Create your views here.

class ReviewView(View):
    def get(self,request):
        form = ReviewForm()

        return render(request,'reviews/index.html',{
            "form" : form
        })
    
    def post(self,request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/show')
        
        return render(request,'reviews/index.html',{
            "form" : form
        })
    

# Get and Post request
class NewReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = '/ew'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# Create View same as that of above
class NewNewReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/index.html'
    success_url = '/show'


class TemplateBaseView(TemplateView):
    template_name = "reviews/show.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("show")
        context['message'] = "This Works!"
        return context

# class AllReviewView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["reviews"] = Review.objects.all()
#         return context
    
class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = Review.objects.get(id = kwargs['id'])
        return context
    
# Single review
class SingleReviewDetailView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review





    
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__lte=9)
        return data
    




# def index(request): 
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
            # username = form.cleaned_data['username']
            # review_text = form.cleaned_data['review_text']
            # rating = form.cleaned_data['rating']
            # review = Review(user_name = username,review_text = review_text,rating=rating)
            # review.save()
            # form.save()
            # print(form.cleaned_data)
            # return HttpResponseRedirect('/show')
    
        # name = request.POST['name']
        # if name == ""html:
        #     return render(request,'reviews/index.html',{
        #         "has_error" : True
        #     })
        # print(name)
        # return HttpResponseRedirect('/show')
    # else:
    #     form = ReviewForm()
    # return render(request,'reviews/index.html',{
        # "has_error": False
    #     "form" : form
    # })


def show(request):
    return render(request,'reviews/show.html')
