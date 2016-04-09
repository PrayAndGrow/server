from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from brainfood.serializers import BrainBitSerializer
from brainfood.models import BrainBit


class BrainFoodSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BrainBit.objects.all()
    serializer_class = BrainBitSerializer