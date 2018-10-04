from django.shortcuts import render
from django.db.models import Q
from products.models import GiftCard, Product, ProductPrice
from products.serializers import GiftCardSerializer, ProductSerializer, ProductPriceSerializer, GetPriceSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from djangorestframework_camel_case.util import underscoreize

# Create your views here.

class GiftCardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows gift cards to be viewed or edited.
    """
    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductPriceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product price changes to be viewed or edited.
    """
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer


@api_view()
def get_price(request):
    """
    View that returns a products price based on the product code, date and optional gift card code.
    """
    data = underscoreize(data=request.query_params)
    params = GetPriceSerializer(data=data)
    params.is_valid(raise_exception=True)

    price = get_product_price(
        date=params.data['date'],
        product_code=params.data['product_code'],
        gift_card_code=params.data.get('gift_card_code')
    )

    return Response({
        'price': price,
    })

def get_product_price(product_code, date, gift_card_code):
    product = Product.objects.get(code=product_code)
    price = product.price

    product_price = (ProductPrice.objects
                        .filter(Q(product=product.id)
                            & Q(date_start__lte=date)
                            & (Q(date_end__isnull=True) | Q(date_end__gte=date)))
                        .first())

    if product_price:
        price = product_price.price

    gift_code = (GiftCard.objects
                    .filter(Q(code=gift_card_code)
                        & Q(date_start__lte=date)
                        & (Q(date_end__isnull=True) | Q(date_end__gte=date)))
                    .first())

    if gift_code:
        # new_price = price - gift_code.amount
        # price = new_price if new_price > 0 else 0
        price = max(0, price - gift_code.amount)

    return '${0:.2f}'.format(price / 100)
