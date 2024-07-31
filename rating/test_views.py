from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Rating


class TestRateView(TestCase):
    """
    Test for rating a post.
    """
    def setUp(self):
        """
        Set up the test environment with a user, a post, and a test client.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            header='Test Header',
            text='Test Content'
        )
        self.client = Client()

    def test_rate(self):
        """
        Test rating functionality by checking rating creation and update.
        """
        self.client.login(username='testuser', password='testpassword')
        
        # Rate the post with 4
        response = self.client.get(reverse('rate', args=[self.post.id, 4]))
        self.assertEqual(response.status_code, 200)
        rating = Rating.objects.get(post=self.post, user=self.user)
        self.assertEqual(rating.rating, 4)

        # Rate the post with 3
        response = self.client.get(reverse('rate', args=[self.post.id, 3]))
        self.assertEqual(response.status_code, 200)
        rating = Rating.objects.get(post=self.post, user=self.user)
        self.assertEqual(rating.rating, 3)
    