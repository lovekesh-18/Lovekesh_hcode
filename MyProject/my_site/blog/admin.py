from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    list_filter = ('author','date','tag')
    list_display = ('title','author','date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name','post')

admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Comment,CommentAdmin)