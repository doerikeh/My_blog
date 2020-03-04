from django.db import models
from datetime import datetime
from django.utils.html import format_html

class BlogCategory(models.Model):
    blog_category = models.CharField(max_length=300)
    image_category = models.ImageField(upload_to='images/blog/', blank=True)
    category_summary = models.CharField(max_length=300)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.blog_category

    def image_tag(self):
        return format_html('<img href="{0}" src="{0}" width="70" height="50" />'.format(self.image_category.url))

    image_tag.allow_tags = True
    image_tag.short_description = 'Image'



class BlogSeries(models.Model):
    blog_series = models.CharField(max_length=200)
    image_series = models.ImageField(upload_to='images/blog/series/', blank=True)
    blog_category = models.ForeignKey(BlogCategory, verbose_name="Categories", default=1, on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Series"
    
    def __str__(self):
        return self.blog_series

class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published = models.DateTimeField("date published", default=datetime.now)
    blog_series = models.ForeignKey(BlogSeries, on_delete=models.SET_DEFAULT, default=1, verbose_name="Series")
    blog_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.title