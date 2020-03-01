from django.contrib import admin
from .models import Blog, BlogCategory, BlogSeries
from tinymce.widgets import TinyMCE
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Date', {"fields": ["title", "published"]}),
        ('Url', {"fields": ["blog_slug"]}),
        ('Series', {"fields": ["blog_series"]}),
        ('Content', {"fields": ["content"]})
    ]

    formfield_overrides ={
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})}
    }

    list_display = ['title', 'published']
    date_hierarchy = 'published'



admin.site.register(BlogSeries)
admin.site.register(BlogCategory)
admin.site.register(Blog, BlogAdmin)