from rest_framework import serializers
from brainfood.models import BrainBit, Tag

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ("tag",)

class BrainBitSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = BrainBit
        fields = ('title', 'url', 'type', 'description', 'image', 'duration', 'tags')
        # fields = "__all__"

