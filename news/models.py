import uuid

from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=20,
        validators=[
            MinLengthValidator(6),
            MaxLengthValidator(20),
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    cover = models.ImageField(upload_to='news/covers/%Y/%m/%d/')

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(12),
            MaxLengthValidator(64),
        ]
    )
    description = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(0),
            MaxLengthValidator(100),
        ]
    )
    body = models.CharField(
        max_length=5000,
        validators=[
            MinLengthValidator(100),
            MaxLengthValidator(5000),
        ]
    )
    body_is_html = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
