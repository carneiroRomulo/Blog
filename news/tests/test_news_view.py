from django.urls import resolve, reverse
from news import views

from .test_news_base import NewsTestBase


class NewsHomeViewTest(NewsTestBase):
    def test_news_home_view_function_is_correct(self):
        view = resolve(reverse('news:home'))
        self.assertIs(view.func, views.home)

    def test_news_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('news:home'))
        self.assertEqual(response.status_code, 200)

    def test_news_home_view_loads_correct_template(self):
        response = self.client.get(reverse('news:home'))
        self.assertTemplateUsed(response, 'news/pages/home.html')
