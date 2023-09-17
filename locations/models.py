from django.db import models
import uuid


class Country(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class State(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        # Specify unique_together as a list of tuples
        unique_together = ('name', 'country')

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        # Specify unique_together as a list of tuples
        unique_together = ('name', 'state')

    def __str__(self):
        return self.name
