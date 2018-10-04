from rest_framework import status
from rest_framework.test import APITestCase


class PriceTests(APITestCase):
    def test_get_price_with_black_friday_discount_and_gift_code(self):
        url = '/api/get-price'
        data = {
            'productCode': 'big_widget',
            'giftCardCode': '10OFF',
            'date': '2018-11-23'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$790.00')

    def test_bad_product_code(self):
        url = '/api/get-price'
        data = {
            'productCode': 'error',
            'giftCardCode': '10OFF',
            'date': '2018-11-23'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['product_code'], ["No product with this code exists"])

    def test_bad_gift_card_code(self):
        url = '/api/get-price'
        data = {
            'productCode': 'big_widget',
            'giftCardCode': 'FREE',
            'date': '2018-11-23'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['gift_card_code'], ["No gift card with this code exists"])

    def test_get_price_before_black_friday_sale(self):
        url = '/api/get-price'
        data = {
            'productCode': 'big_widget',
            'giftCardCode': '10OFF',
            'date': '2018-11-11'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$990.00')

    def test_get_price_after_black_friday_sale(self):
        url = '/api/get-price'
        data = {
            'productCode': 'big_widget',
            'giftCardCode': '10OFF',
            'date': '2018-11-26'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$990.00')

    def test_sm_widget_get_price_black_friday_sale_with_gift_card(self):
        url = '/api/get-price'
        data = {
            'productCode': 'sm_widget',
            'giftCardCode': '50OFF',
            'date': '2018-11-24'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$0.00')

    def test_sm_widget_get_price_black_friday_sale_without_gift_card(self):
        url = '/api/get-price'
        data = {
            'productCode': 'sm_widget',
            'date': '2018-11-24'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$0.00')

    def test_big_widget_get_price_december_gift_card(self):
        url = '/api/get-price'
        data = {
            'productCode': 'big_widget',
            'giftCardCode': '250OFF',
            'date': '2018-12-25'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$750.00')

    def test_sm_widget_get_price_december_gift_card(self):
        url = '/api/get-price'
        data = {
            'productCode': 'sm_widget',
            'giftCardCode': '250OFF',
            'date': '2018-12-25'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$0.00')

    def test_big_widget_get_price_2019_with_gift_card(self):
        url = '/api/get-price'
        data = {
            'productCode': 'big_widget',
            'giftCardCode': '50OFF',
            'date': '2019-01-01'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$1150.00')

    def test_sm_widget_get_price_2019_with_gift_card(self):
        url = '/api/get-price'
        data = {
            'productCode': 'sm_widget',
            'giftCardCode': '50OFF',
            'date': '2019-01-01'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$75.00')

    def test_big_widget_get_price_2019_without_gift_card(self):
        url = '/api/get-price'
        data = {
            'productCode': 'big_widget',
            'date': '2019-01-01'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$1200.00')

    def test_sm_widget_get_price_2019_without_gift_card(self):
        url = '/api/get-price'
        data = {
            'productCode': 'sm_widget',
            'date': '2019-01-01'
        }
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '$125.00')
