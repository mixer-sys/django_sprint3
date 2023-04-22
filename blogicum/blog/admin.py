from django.contrib import admin
from django.db import models
from django.forms import Textarea
from blog.models import Category, Location, Post


class ViewSettings(admin.ModelAdmin):
    list_per_page = 10
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5, 'cols': 45})},
    }


class PostAdmin(ViewSettings):
    list_display = (
        'title', 'text', 'category', 'is_published', 'author', 'location',
        'pub_date', 'created_at'
    )
    list_editable = (
        'text', 'pub_date',
        'author', 'location', 'category',
        'is_published'
    )
    search_fields = ('title', 'text',)
    list_filter = ('category', 'author', 'location',
                   'is_published', 'created_at')
    list_display_links = ('title',)
    empty_value_display = 'Не задано'


class LocationAdmin(ViewSettings):
    list_display = (
        'name', 'is_published', 'created_at'
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('name',)
    list_filter = ('created_at', 'is_published', 'name')
    empty_value_display = 'Не задано'


class CategoryAdmin(ViewSettings):
    list_display = (
        'title', 'description', 'slug',
        'is_published', 'created_at'
    )
    list_editable = (
        'description',
        'slug',
        'is_published',
    )
    search_fields = ('title', 'description', 'slug')
    list_filter = ('created_at', 'is_published', 'slug')
    empty_value_display = 'Не задано'


admin.site.register(Post, PostAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
