from django.core.exceptions import ValidationError
from news.models import News
from parameterized import parameterized

from .test_news_base import NewsTestBase


class NewsModelTest(NewsTestBase):
    def setUp(self) -> None:
        self.news = self.make_news()
        return super().setUp()

    @parameterized.expand([
        ('title', 64),
        ('description', 100),
        ('body', 5000),
    ])
    def test_news_model_fields_max_lenght(self, field, max_length):
        setattr(self.news, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.news.full_clean()

    @parameterized.expand([
        ('title', 6),
        ('description', 12),
        ('body', 100),
    ])
    def test_news_model_fields_min_lenght(self, field, min_length):
        setattr(self.news, field, 'A' * (min_length - 1))
        with self.assertRaises(ValidationError):
            self.news.full_clean()

    def test_news_model_body_is_html(self):
        news = News(
            cover='cover.png',
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(username='newuser'),
            title='News Title',
            description='News Description',
            body='A' * 100,
        )
        news.full_clean()
        news.save()
        self.assertFalse(getattr(news, 'body_is_html'))

    def test_news_string_representation(self):
        needed = 'Testing Representation'
        self.news.title = needed
        self.news.full_clean()
        self.news.save()
        self.assertEqual(str(self.news), needed)


class NewsCategoryModelTest(NewsTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Category Testing')
        return super().setUp()

    def test_news_category_model_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_news_category_model_name_max_length_is_20_chars(self):
        self.category.name = 'A' * 21
        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_news_category_model_name_min_length_is_6_chars(self):
        self.category.name = 'A' * 5
        with self.assertRaises(ValidationError):
            self.category.full_clean()
