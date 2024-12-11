from rest_framework import serializers
from .models import Category, Product, ProductImage, Review


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['url']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'username', 'rating', 'text']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    category = serializers.CharField()
    class Meta:
        model = Product
        fields = ['name', 'images', 'reviews', 'description', 'category', 'affiliate_link']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        reviews_data = validated_data.pop('reviews')
        category = validated_data.pop('category')
        print(category)

        cat, created = Category.objects.get_or_create(category_name = category)
        product = Product.objects.create(**validated_data, category=cat)

        # Save images
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)

        # Save reviews
        for review_data in reviews_data:
            Review.objects.create(product=product, **review_data)

        return product