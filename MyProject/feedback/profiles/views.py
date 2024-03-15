from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from  .forms import *
from .models import UploadFile
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.

# class UploadFileClass(View):
#     def get(self,request):
#         form = ProfileForm()
#         return render(request,'profiles/profile.html',locals())
    
#     def post(self, request):
#         form = ProfileForm(request.POST , request.FILES)
        
#         if form.is_valid():
#             image = request.FILES['user_image']
#             profile = UploadFile(image = image)
#             profile.save()
#             print("form submitted")
#             return HttpResponse("Form Submitted")
#         # print(request.FILES.get('file'))
#         return HttpResponse("My File")

class UploadFileClass(CreateView):
    template_name = 'profiles/profile.html'
    model = UploadFile
    fields = '__all__'
    success_url = '/profile'

class ProfileView(ListView):
    model = UploadFile
    template_name = "profiles/show.html"
    context_object_name = "profiles"