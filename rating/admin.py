from django.contrib import admin
from .models import Rating, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('header', 'text')
    search_fields = ('header', 'text')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'rating')
    list_filter = ('post', 'rating')
    search_fields = ('user__username', 'post__header')