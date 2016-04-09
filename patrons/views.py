import datetime

from django.db.models import Q
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


@api_view(['GET', 'POST'])
def patron_search(request):
    """
    Search for patrons in the neighbourhood and for today.
    """
    today = datetime.date.today()
    patrons = Patron.objects.filter(Q(reminiscence=today) | Q(canonisation=today))
    serializer = PatronSerializer(patrons, many=True)
    return Response({'response': serializer.data})
