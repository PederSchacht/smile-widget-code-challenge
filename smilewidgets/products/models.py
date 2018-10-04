from django.db import models


class GiftCard(models.Model):
    code = models.CharField(max_length=30)
    amount = models.PositiveIntegerField(help_text='Value of gift card in cents')
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.code, self.formatted_amount)

    @property
    def formatted_amount(self):
        return '${0:.2f}'.format(self.amount / 100)


class Product(models.Model):
    name = models.CharField(max_length=25, help_text='Customer facing name of product')
    code = models.CharField(max_length=10, help_text='Internal facing reference to product')
    price = models.PositiveIntegerField(help_text='Price of product in cents')

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='Product effected by a price change')
    name = models.CharField(max_length=35, help_text='Name that describes the price change')
    price = models.PositiveIntegerField(help_text='New price of product in cents')
    date_start = models.DateField(help_text='Start date of price change')
    date_end = models.DateField(blank=True, null=True, help_text='End date of price change')

    def __str__(self):
        return f"{self.product.name}: {self.formatted_price} {self.formatted_date_range}"

    @property
    def formatted_price(self):
        return '${0:.2f}'.format(self.price / 100)

    @property
    def formatted_date_range(self):
        if self.date_end:
            return f"for {self.date_start} through {self.date_end}"
        return f"from {self.date_start}"
