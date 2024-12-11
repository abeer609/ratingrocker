from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['url', 'product']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'image')
    search_fields = ("category_name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ("name",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'title')
    search_fields = ("title",)
    

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ("name",)

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    search_fields = ("title",)

@admin.register(PostReview)
class PostReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'title')

admin.site.site_header = "Rating Rocker Admin"
admin.site.site_title = "Rating Rocker Admin"
