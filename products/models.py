from django.db import models
from django.contrib.auth.models import User


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
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    rate = models.ManyToManyField(
        User, related_name='product_rate', blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='review')
    comment = models.TextField(max_length=254)
    rate = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Comments ordered from last to first """
        ordering = ['created_on']

    def __str__(self):
        return str(self.id)
