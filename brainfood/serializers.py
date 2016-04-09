from rest_framework import serializers
from brainfood.models import BrainBit

class BrainBitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrainBit
        fields = ('title', 'url', 'type', 'description', 'image', 'duration')