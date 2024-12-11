"""reviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from myAdmin.sitemap import BlogSitemap, ProductSitemap, ReviewSitemap, CategorySitemap
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path


def trigger_error(request):
    division_by_zero = 1 / 0


sitemaps = {
    "blogs": BlogSitemap,
    "products": ProductSitemap,
    "reviews": ReviewSitemap,
    "categories": CategorySitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
    path("user/", include("user.urls")),
    path("", home, name="home"),
    path("about_usTell/", about_us, name="aboutus"),
    path("all-category", all_category, name="all_category"),
    path("blog", blog, name="blog"),
    path("blog/<int:blog_id>_<slug>/", blog_detail, name="blog_detail"),
    path("privacy-policy", privacy_policy, name="privacy_policy"),
    path("terms-and-conditions", terms, name="terms"),
    path("faq", faq, name="faq"),
    path("search", search, name="search"),
    path("about_us", about_us, name="about_us"),
    path(
        "category/<int:category_id>_<slug>/",
        category_products,
        name="category_products",
    ),
    path(
        "product-review/<int:product_id>_<slug:product_slug>/",
        product_review,
        name="product_review",
    ),
    path("read-review/<int:product_id>_<slug>/", read_review, name="read_review"),
    path("accounts/", include("allauth.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('', include('myAdmin.urls')),
    path("robots.txt", include("robots.urls")),
    # path('product-review/<str:review_text>/reviews-page.html', custom_redirect_view, name='custom_redirect')
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "common.django_web.views.not_found_page.Error404View"
