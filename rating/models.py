from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
# Source: https://medium.com/p/e1deff03bb1c

class Post(models.Model):
    """
    Represents a post with a header and text.
    """
    header = models.CharField(max_length=100, default="Header")
    text = models.TextField()

    def average_rating(self) -> float:
        """
        Calculate the average rating for the post.
        """
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        """
        Return a string representation of the post with its average rating.
        """
        return f"{self.header}: {self.average_rating()}"


class Rating(models.Model):
    """
    Represents a rating given by a user to a post.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of the rating.
        """
        return f"{self.post.header}: {self.rating}"
