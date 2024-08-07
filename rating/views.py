from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Rating, Post


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Render a list of posts with the current user's ratings.
    """
    if not request.user.is_authenticated:
        raise PermissionDenied
    posts = Post.objects.all()
    for post in posts:
        rating = Rating.objects.filter(post=post, user=request.user).first()
        post.user_rating = rating.rating if rating else 0
    return render(request, "rating/ratings.html", {"posts": posts})


def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
    """
    Update or create a rating for a post by the current user.
    """
    post = Post.objects.get(id=post_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return index(request)
