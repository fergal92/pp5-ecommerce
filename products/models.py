from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)])
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(default='images/default.png' )

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f'Review by {self.user.user.username} on {self.product.name}' # not working yet
