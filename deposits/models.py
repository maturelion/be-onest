import uuid
from django.db import models
from users.models import User

STATUS = [
    ["SUCCESSFUL", "SUCCESSFUL"],
    ["PENDING", "PENDING"],
    ["FAILED", "FAILED"],
    ["CANCELED", "CANCELED"],
    ["HOLD", "HOLD"],
]


class Deposit(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField( default=0)
    status = models.CharField(max_length=50, choices=STATUS, default="PENDING")
    address_used = models.CharField(max_length=225)
    wallet = models.TextField()
    tx_hash = models.CharField(max_length=225, blank=True)
    ref_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __repr__ (self):
        return '<Deposit %s>' % self.user.username

    def __str__(self):
        return "Deposit " + self.user.username + " => " + str(self.amount)
