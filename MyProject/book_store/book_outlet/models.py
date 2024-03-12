from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length = 100)
    pin_code = models.CharField(max_length = 50)
    city = models.CharField(max_length = 40)

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    address = models.OneToOneField(Address,on_delete = models.CASCADE,null = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    


class Book(models.Model):
    title = models.CharField(max_length = 60)
    rating = models.IntegerField(validators = [
        MinValueValidator(1),MaxValueValidator(10)
    ])
    author = models.ForeignKey(Author,on_delete = models.CASCADE,null=True)
    # author = models.CharField(null=True,max_length = 100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank = True,null=False)
    #editable False
    published_country = models.ManyToManyField(Country)
    def get_absolute_url(self):
        return reverse("detail-page", args=[self.slug])
    
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
