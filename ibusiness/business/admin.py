from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Category, Post

User = get_user_model()
# Register your models here.

# for configuration of Category admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
