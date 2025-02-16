from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        # Ensures a product is only added once per user
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
