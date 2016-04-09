from rest_framework import viewsets
from .models import Patron
from .serializers import PatronSerializer


class PatronSet(viewsets.ModelViewSet):
    """
    API endpoint for Patrons
    """
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer
