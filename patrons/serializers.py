from rest_framework import serializers
from .models import Patron


class PatronSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patron
        fields = ('name', 'url', 'reminiscence', 'canonisation')
