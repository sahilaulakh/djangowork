from django.contrib import admin

# Register your models here.
from blog_posts.models import blog_posts

admin.site.register(blog_posts)