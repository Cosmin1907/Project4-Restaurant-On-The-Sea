from django.contrib import admin
from .models import Rating, Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Post models.
    """
    list_display = ('header', 'text')
    search_fields = ('header', 'text')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Rating models.
    """
    list_display = ('user', 'post', 'rating')
    list_filter = ('post', 'rating')
    search_fields = ('user__username', 'post__header')