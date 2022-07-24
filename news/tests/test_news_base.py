from django.test import TestCase
from news.models import Category, News, User


class NewsMixin:
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name='Romulo',
        last_name='Carneiro',
        username='admin',
        password='123456',
        email='username@gmail.com',
    ): return User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password,
        email=email,
    )

    def make_news(
        self,
        cover='cover.png',
        category={},
        author={},
        title='News Title 1',
        description='News Description',
        body='A' * 100,
        body_is_html=False,
    ):
        return News.objects.create(
            cover=cover,
            category=self.make_category(**category),
            author=self.make_author(**author),
            title=title,
            description=description,
            body=body,
            body_is_html=body_is_html,
        )

    def make_news_batch(self, quantity):
        news = []
        for i in range(quantity):
            kwargs = {'author': {'username': f'u{i}'}}
            news = self.make_news(**kwargs)
            news.append(news)
        return news


class NewsTestBase(TestCase, NewsMixin):
    def setUp(self) -> None:
        return super().setUp()
