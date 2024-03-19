from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from datetime import date
from .models import *
from .forms import CommentForm
from django.views.generic import TemplateView,DetailView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse
from django.views.generic import View
from django.http import HttpResponseRedirect
all_post = [
#     {
#         "slug" : "Nature-At-Its-Best",
#         "image" : "tree1.jpg",
#         "author" : "Lovekesh",
#         "date" : date(2024, 3, 8),
#         "title" : "Nature At Its Best",
#         "excerpt" : "Some quick example text to build on the card title and make up the bulk of the card's content.",
#         "content": """ 
# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.
# """
#     },
#     {
#         "slug" : "Programming-Is-Great",
#         "image" : "mountain.jpg",
#         "author" : "Lovekesh",
#         "date" : date(2024, 3, 8),
#         "title" : "Programming Is Great",
#         "excerpt" : "Some quick example text to build on the card title and make up the bulk of the card's content.",
#         "content": """ 
# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.
# """
#     },
#     {
#         "slug" : "Mountain-Hiking",
#         "image" : "mountains.jpg",
#         "author" : "Lovekesh",
#         "date" : date(2024, 3, 8),
#         "title" : "Mountain Hiking",
#         "excerpt" : "Some quick example text to build on the card title and make up the bulk of the card's content.",
#         "content": """ 
# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

# Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.
# """
#     }
]

# def get_date(all_post):
#     return all_post['date']

# Create your views here.

# def starting_page(request):
#     latest_post = Post.objects.all().order_by("date")[:3]
    # sorted_posts = sorted(all_post,key=get_date)
    # latest_post = sorted_posts[-3:]
    # return render(request,'blog/index.html',{
    #     "post_s":latest_post
    # })

class StartPage(ListView):
    template_name = "blog/index.html"
    model = Post 
    ordering = ["-date"]
    context_object_name = "post_s"

    def get_queryset(self):
        query_data = super().get_queryset()
        data = query_data[:3]
        return data

# def posts(request):
#     all_post = Post.objects.all()
#     return render(request,'blog/all_posts.html',{
#         "all_posts" : all_post
#     })

class All_Post(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    context_object_name = "all_posts"

# def post_detail(request,slug):
#     identified_post = get_object_or_404(Post, slug = slug)
    # identified_post = next(post for post in all_post if post['slug'] == slug)
    # return render(request,'blog/post_detail.html',{
    #     "post":identified_post,
    #     "post_tag" : identified_post.tag.all()
    # })

# class Post_Detail(DetailView):
#     template = 'blog/post_detail.html'
#     model = Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_tag'] = self.object.tag.all()
#         context['form'] = CommentForm()
#         return context

    
class Post_Detail(View):
    def is_saved_post(self,request,post_id):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        
        return is_saved_for_later

    def get(self, request,slug):
        post = Post.objects.get(slug = slug)
        form = CommentForm()
        context = {
            'post' : post,
            'form' : form,
            'comments' : post.posts.all(),
            'post_tag' : post.tag.all(),
            'save_post' : self.is_saved_post(request,post.id)
        }
        return render(request,'blog/post_detail.html', context)
    
    def post(self,request,slug):
        post = Post.objects.get(slug = slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            data = form.save(commit = False)
            data.post = post
            data.save()
            return HttpResponseRedirect(reverse('post-detail-page' , args=[slug]))
        comments = post.posts.all()
        post_tag = post.tag.all()
        save_post = self.is_saved_post(request,post.id) 
        return render(request,'blog/post_detail.html',locals())


# class Post_Detail(FormView):
#     template_name = 'blog/post_detail.html'
#     form_class = CommentForm

#     def get_success_url(self):
#         slug = self.kwargs['slug']
#         return reverse("post-detail-page",args=[slug])
    
#     def form_valid(self, form):
#         form_data = form.save(commit = False)
#         form_data.post = Post.objects.get(slug = self.kwargs['slug'])
        # if form_data:
        # form_data.save()
        # return super().form_valid(form)
        # else:
        #     form.add_error(None,'Please Enter correct data')
        #     return self.form_invalid(form)
    

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in = stored_posts)
            context['posts'] = posts
            context['has_posts'] = True
        
        return render(request,'blog/read-posts.html',context)


    def post(self,request):
        stored_posts = request.session.get('stored_posts')

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST.get('post_id'))

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session['stored_posts'] = stored_posts
        
        return HttpResponseRedirect('/')
        

    
 
def error_404(request,exception):
    return render(request,'404.html')