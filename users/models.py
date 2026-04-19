from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    points = models.IntegerField(default=1000)  # 預設給1000點方便測試

class PointTransaction(models.Model):
    TYPE_CHOICES = [
        ("topup", "Top Up"),
        ("redeem", "Redeem"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)