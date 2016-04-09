from django.db import models


class Place(models.Model):
    """
    Representation of a place that could notice an activity
    of one saint.
    """
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Activity(models.Model):
    """
    An activity that can have a patron attached.
    """
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Patron(models.Model):
    """
    A model representing one saint
    """
    name = models.CharField(max_length=1024)
    url = models.URLField()
    reminiscence = models.DateField(blank=True, null=True)
    canonisation = models.DateField(blank=True, null=True)
    places = models.ManyToManyField(Place, blank=True)
    activities = models.ManyToManyField(Activity, blank=True)

    def __str__(self):
        return self.name
