from django.db import models
from django.contrib.auth.models import User


class Kharcha(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=64, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description}"
