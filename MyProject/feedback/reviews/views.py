from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.views import View
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
        # if name == "":
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
