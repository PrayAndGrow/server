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
    url = models.URLField(max_length=200)
    type = models.CharField(max_length=2, choices=TYPES)
    description = models.CharField(max_length=512)
    image = models.URLField(max_length=200)
    duration = models.DurationField

    def __str__(self):
        return self.title + " " + self.description + ", " + self.type


class Tag(models.Model):
    """
    A single tag for the BrainBit
    """
    tag = models.CharField(max_length=64)
    brain_bits = models.ManyToManyField(BrainBit)

    def __str__(self):
        return self.tag
