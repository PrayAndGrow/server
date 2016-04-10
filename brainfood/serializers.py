from rest_framework import serializers
from brainfood.models import BrainBit, Tag

class TagSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Tag
        fields = ("tag","id")


class BrainBitSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    tags = TagSerializer(many=True)
    class Meta:
        model = BrainBit
        fields = ('id','title', 'url', 'type', 'description', 'image', 'duration', 'tags')


# class SurpriseMeSerializer():

