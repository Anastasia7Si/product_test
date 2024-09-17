from django.db import models


class Product(models.Model):
    """Модель продукта."""

    name = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False
        )
    description = models.TextField()
    price = models.PositiveIntegerField()
