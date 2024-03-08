from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string

my_challenges = {
    "january" : "January Task",
    "february" : "February Task",
    "march" : "March Task",
    "april": "April Task",
    "may" : "May Task",
    "june" : "June Task",
    "july" : "July Task",
    "august" : None
}

# Create your views here.

def index(request):
    months = list(my_challenges.keys())
    return render(request,"monthly_challenges/index.html",{
        "months": months
    })
    

def all_function_number(request,month):
    keys_list = list(my_challenges.keys())
    if(month > len(keys_list)):
        return HttpResponseNotFound("Bhai ye month exist hi nhi krta")
    month = keys_list[month - 1]
    redirect_url = reverse("month-url-name", args=[month])  #/challenges/month/
    return HttpResponseRedirect(redirect_url)

def all_function(request,month):
    try:
        message = my_challenges[month]
        return render(request,"monthly_challenges/challenges.html",{
            "text": message
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponse(response_data)
        # return HttpResponseNotFound("Aree bhai ye url mere pass nhi hai")
    
        