from django.db import models
import datetime

class Tag(models.Model):
    """
    A single tag for the BrainBit
    """
    tag = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.tag


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
    url = models.URLField(max_length=200, unique=True)
    type = models.CharField(max_length=2, choices=TYPES)
    description = models.CharField(blank=True, max_length=512)
    image = models.URLField(blank=True, max_length=200)
    duration = models.DurationField(default="5:0")
    created = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title + ", " + self.type
