from django.db import models


class Orders(models.Model):
    order_code = models.PositiveIntegerField(unique=True, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    id_seller = models.PositiveIntegerField(null=False)
    id_channel = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.order_code, self.date, self.id_seller, self.id_channel}"


class OrdersProdcut(models.Model):
    id_product = models.PositiveIntegerField(null=False)
    id_orders = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f"{self.id_product, self.id_orders}"


class ProductOrders(models.Model):
    amount = models.IntegerField(max_digits=10, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"{self.amount, self.price}"
