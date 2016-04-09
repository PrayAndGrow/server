from django.db import models


class BrainBit(models.Model):
    """
    A single entry on the list of proposals
    """
    TYPES = (
        ('AR', 'Article'),
        ('VI', 'Video'),
        ('PO', 'Podcast')
    )
    title = models.CharField(max_length=64)
    url = models.URLField
    type = models.CharField(max_length=2, choices=TYPES)
    description = models.TextField
    image = models.URLField
    duration = models.DurationField


class Tag(models.Model):
    """
    A single tag for the BrainBit
    """
    tag = models.CharField(max_length=64)
    brain_bits = models.ManyToManyField(BrainBit)
