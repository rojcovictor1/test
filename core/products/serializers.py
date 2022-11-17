from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class ProductSerializer(serializers.ModelSerializer[Product]):
    images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False,
                                     use_url=False), write_only=True
    )

    def to_representation(self, instance):
        """ Convert author_id to username """
        field = super().to_representation(instance)
        user = User.objects.get(id=field['author'])
        field['author'] = user.username
        return field

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'price',
            'images',
            'created',
            'author',
            'uploaded_images',
        ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            product_image = ProductImage.objects.create(product=product, image=image)

        return product



