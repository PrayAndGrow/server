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
