from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "author")
    list_filter = ("published_date", "author")
    search_fields = ("title",)