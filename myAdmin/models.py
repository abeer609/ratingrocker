from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from meta.models import ModelMeta


# Create your models here.
class Category(models.Model, ModelMeta):

    category_name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='category_images/')
    image = models.URLField(default="", blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, max_length=500)

    _metadata = {
        "title": "category_name",
        "image": "get_meta_image"
    }

    def __str__(self):
        return self.category_name

    def get_meta_image(self):
        if self.image:
            return self.image

    def get_absolute_url(self):
        return reverse("category_products", args=[self.id, self.slug])


@receiver(pre_save, sender=Category)
def slugify_category(sender, instance, **kwargs):
    if instance.category_name:
        instance.slug = slugify(instance.category_name)



class Product(models.Model, ModelMeta):
    name = models.CharField(max_length=200)
    description = models.TextField()
    affiliate_link = models.URLField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, limit_choices_to={'username__in': ['ayush', 'admin']})
    slug = models.SlugField(null=True, blank=True, max_length=500)

    _metadata = {
        "title": "name",
        "description": "description",
        "image": "image"
    }

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_review", args=[self.id, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    url = models.URLField()

@receiver(pre_save, sender=Product)
def slugify_product(sender, instance, **kwargs):
    if instance.name:
        instance.slug = slugify(instance.name)


class Review(models.Model, ModelMeta):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=120)
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, max_length=500)

    _metadata = {
        "title": "title",
        "description": "text",
        "image": "image"
    }

    def __str__(self):
        return f"Review for {self.product.name} by {self.title}"

    def get_author(self):
        return self.user

    def get_absolute_url(self):
        return reverse("read_review", args=[self.id, self.slug])


@receiver(pre_save, sender=Review)
def slugify_review(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)


class BlogPost(models.Model, ModelMeta):
    title = models.CharField(max_length=200)
    content = RichTextField()
    # featured_image = models.ImageField(upload_to='blog_featured_images/', null=True, blank=True)
    featured_image = models.URLField(default="", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.title

    _metadata = {
        "title": "title",
        "description": "content",
        "image": "image"
    }

    def get_author(self):
        return self.author

    def get_absolute_url(self):
        return reverse("blog_detail", args=[self.id, self.slug])


@receiver(pre_save, sender=BlogPost)
def slugify_blog_post(sender, instance, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)


class Contact(models.Model, ModelMeta):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, max_length=500)

    def __str__(self):
        return self.name

    _metadata = {
        "title": "subject",
        "description": "message",
    }

class PostReview(models.Model, ModelMeta):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.CharField(max_length = 50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, max_length=500)

    def __str__(self):
        return f"Review for {self.product.name} by {self.title}"
