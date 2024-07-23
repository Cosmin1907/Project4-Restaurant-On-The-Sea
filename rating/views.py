from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Rating, Post

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    for post in posts:
        rating = Rating.objects.filter(post=post, user=request.user).first()
        post.user_rating = rating.rating if rating else 0
    return render(request, "rating/ratings.html", {"posts": posts})

def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
    print(f"Received request to rate post {post_id} with rating {rating}")
    post = Post.objects.get(id=post_id)
    Rating.objects.filter(post=post, user=request.user).delete()
    post.rating_set.create(user=request.user, rating=rating)
    return index(request)