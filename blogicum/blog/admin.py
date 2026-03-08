from django.contrib import admin

from .models import Category, Comment, Location, Post


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_filter = ('is_published',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'category', 'location',
        'pub_date', 'is_published', 'created_at',
    )
    list_editable = ('is_published', 'category')
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'category', 'location')
    inlines = (CommentInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'post', 'created_at')
    search_fields = ('text',)
    list_filter = ('author',)
