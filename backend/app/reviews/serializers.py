from rest_framework import serializers
from .models import ProductReview
from products.serializers import ProductInfoSerializer


class ProductReviewListSerializer(serializers.ModelSerializer):
    product_info = ProductInfoSerializer(source="product", read_only=True)

    class Meta:
        model = ProductReview
        fields = "__all__"


class ProductReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = "__all__"
        read_only_fields = ["status", "created_at", "updated_at"]

