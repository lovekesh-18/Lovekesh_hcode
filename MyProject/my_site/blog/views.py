from django.shortcuts import render
from datetime import date

all_post = [
    {
        "slug" : "Nature-At-Its-Best",
        "image" : "tree1.jpg",
        "author" : "Lovekesh",
        "date" : date(2024, 3, 8),
        "title" : "Nature At Its Best",
        "excerpt" : "Some quick example text to build on the card title and make up the bulk of the card's content.",
        "content": """ 
Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.
"""
    },
    {
        "slug" : "Programming-Is-Great",
        "image" : "mountain.jpg",
        "author" : "Lovekesh",
        "date" : date(2024, 3, 8),
        "title" : "Programming Is Great",
        "excerpt" : "Some quick example text to build on the card title and make up the bulk of the card's content.",
        "content": """ 
Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.
"""
    },
    {
        "slug" : "Mountain-Hiking",
        "image" : "mountains.jpg",
        "author" : "Lovekesh",
        "date" : date(2024, 3, 8),
        "title" : "Mountain Hiking",
        "excerpt" : "Some quick example text to build on the card title and make up the bulk of the card's content.",
        "content": """ 
Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.

Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit tenetur tempora delectus optio veniam, laudantium sint esse voluptates debitis repellat rem hic fugiat! Ipsam repellendus quibusdam laudantium doloremque nihil perspiciatis, consequatur nemo dolor dolorem.
"""
    }
]

def get_date(all_post):
    return all_post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_post,key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request,'blog/index.html',{
        "post_s":latest_post
    })

def posts(request):
    return render(request,'blog/all_posts.html',{
        "all_posts" : all_post
    })

def post_detail(request,slug):
    identified_post = next(post for post in all_post if post['slug'] == slug)
    return render(request,'blog/post_detail.html',{
        "post":identified_post
    })

def error_404(request,exception):
    return render(request,'404.html')