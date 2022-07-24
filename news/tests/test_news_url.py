from django.test import TestCase
from django.urls import reverse


class NewsURLsTest(TestCase):
    def test_news_home_url_is_correct(self):
        url = reverse('news:home')
        self.assertEqual(url, '/')

    def test_news_search_url_is_correct(self):
        url = reverse('news:search')
        self.assertEqual(url, '/search/')

    def test_news_category_url_is_correct(self):
        url = reverse('news:category', kwargs={'category_name': 'food'})
        self.assertEqual(url, '/category/food/')
