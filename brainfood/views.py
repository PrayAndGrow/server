from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from brainfood.serializers import BrainBitSerializer, TagSerializer
from brainfood.models import BrainBit, Tag
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from datetime import timedelta


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


@api_view(['POST'])
def surpriseMe(request):
    duration_lt = timedelta(seconds=request.data['duration_lt'])
    bits = BrainBit.objects.filter(type__in=request.data['types']).filter(duration__lt = duration_lt).order_by('-duration').filter(tags__in=request.data['tags']).distinct()
    serializer = BrainBitSerializer(bits, many=True)
    return Response({'response': serializer.data})


