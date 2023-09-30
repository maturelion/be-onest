from django.db import models
import os
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import User


@receiver(post_save, sender=User)
def wallet_create(sender, instance=None, created=False, **kwargs):
    if not os.environ.get('SKIP_SIGNAL_HANDLERS', False):
        if created:
            try:
                Wallet.objects.create(user=instance, balance=0.00)
            except Exception as e:
                print(e)


class Wallet(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user")
    balance = models.FloatField(default=0)

    def __str__(self):
        return "Wallet " + self.user.username + " => " + str(self.balance)