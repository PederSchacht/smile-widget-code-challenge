from products.models import GiftCard, Product, ProductPrice
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class GiftCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GiftCard
        fields = ('id', 'code', 'amount', 'date_start', 'date_end', 'url')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'code', 'price', 'url')


class ProductPriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('id', 'product', 'name', 'price', 'date_start', 'date_end', 'url')


class GetPriceSerializer(serializers.Serializer):
    """
    Validates the get-price API query params.
    """
    product_code = serializers.CharField(max_length=10)
    date = serializers.DateField()
    gift_card_code = serializers.CharField(max_length=30, required=False)

    def validate_product_code(self, code):
        try:
            return Product.objects.get(code=code).code
        except Product.DoesNotExist:
            raise ValidationError("No product with this code exists")

    def validate_gift_card_code(self, code):
        try:
            return GiftCard.objects.get(code=code).code
        except GiftCard.DoesNotExist:
            raise ValidationError("No gift card with this code exists")
