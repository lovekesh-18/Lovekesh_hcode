from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

my_challenges = {
    "january" : "January Task",
    "february" : "February Task",
    "march" : "March Task",
    "april": "April Task",
    "may" : "May Task",
    "june" : "June Task",
    "july" : "July Task",
    "august" : "August Task"
}

# Create your views here.

def index(request):
    months = list(my_challenges.keys())
    list_items = ""
    
    for month in months:
        month_item = month.capitalize()
        redirect_url = reverse("month-url-name",args=[month])
        list_items += f"<li><a href=\"{redirect_url}\">{month_item}</a></li>"
    print(list_items)
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
        return HttpResponse(message)
    except:
        return HttpResponseNotFound("Aree bhai ye url mere pass nhi hai")
    
        