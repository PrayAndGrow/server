from rest_framework import serializers
from brainfood.models import BrainBit, Tag

class TagSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Tag
        fields = ("tag","id")

class BrainBitSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = BrainBit
        fields = ('title', 'url', 'type', 'description', 'image', 'duration', 'tags')

# class SurpriseMeSerializer():

