from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length = 1000)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length = 100)
    excerpt = models.CharField(max_length = 900)
    # image = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="image" , null = True)
    date = models.DateField(auto_now = True)
    slug = models.SlugField(unique = True,db_index = True,null=True,blank = True)
    content = models.TextField(validators = [MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null = True, related_name = "posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length = 100)
    user_email = models.EmailField()
    user_text = models.TextField(max_length = 300)
    post = models.ForeignKey(Post,on_delete = models.CASCADE, related_name = "posts")

    def __str__(self):
        return self.user_name

