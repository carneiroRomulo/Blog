from django.contrib import admin, messages
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.translation import ngettext

from .models import Category, News


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'category', 'status')
    ordering = ['status']
    actions = ['make_published', 'make_withdrawn']
    radio_fields = {"status": admin.HORIZONTAL}

    @admin.action(description='Publish selected News')
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Withdrawn selected News')
    def make_withdrawn(self, request, queryset):
        updated = queryset.update(status='w')
        self.message_user(request, ngettext(
            '%d story was successfully marked as withdrawn.',
            '%d stories were successfully marked as withdrawn.',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
