from rest_framework import serializers
from .models import Patron, Prayer, Place


class PrayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prayer
        fields = ('prayer',)


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('name',)


class PatronSerializer(serializers.HyperlinkedModelSerializer):
    prayer = PrayerSerializer()
    places = PlaceSerializer(many=True)

    class Meta:
        model = Patron
        fields = ('name', 'url', 'reminiscence', 'canonisation', 'prayer', 'places')
