from django.contrib.sitemaps import Sitemap

from myAdmin.models import BlogPost, Product, Review, Category


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Category.objects.all()


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Product.objects.all()


class ReviewSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Review.objects.all()

    def lastmod(self, obj):
        return obj.created_at
