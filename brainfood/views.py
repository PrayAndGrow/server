from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from brainfood.serializers import BrainBitSerializer, TagSerializer
from brainfood.models import BrainBit, Tag


class BrainFoodSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BrainBit.objects.all()
    serializer_class = BrainBitSerializer

class TagSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

