from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Reviews(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews')
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_added",
        null=True)
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Comments ordered from last to first """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.posted_by}"
