import datetime
from functools import reduce

import requests

from django.db.models import Q
from django.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Patron
from .serializers import PatronSerializer


class PatronSet(viewsets.ModelViewSet):
    """
    API endpoint for Patrons
    """
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer


def get_places(lat, lon):
    endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    radius = '100'

    url = '{0}?key={1}&location={2},{3}&radius={4}'.format(endpoint, settings.GOOGLE_PLACES_API_KEY, lat, lon, radius)
    r = requests.get(url)
    names = []
    try:
        json = r.json()
        for entry in json["results"]:
            names.append(entry["name"])

        return names
    except:
        return []


@api_view(['POST'])
def patron_search(request):
    """
    Search for patrons in the neighbourhood and for today.
    """
    today = datetime.date.today()
    if 'latitude' and 'longitude' in request.data:
        places = get_places(request.data['latitude'], request.data['longitude'])

    try:
        patrons = Patron.objects.filter(Q(reminiscence=today) |
            reduce(lambda x, y: x | y, [Q(places__name__icontains=place) for place in places]))
    except UnboundLocalError:
        patrons = Patron.objects.filter(Q(reminiscence=today) | Q(canonisation=today))

    serializer = PatronSerializer(patrons, many=True)
    return Response({'response': serializer.data})
