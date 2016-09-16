from rest_framework import viewsets
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewset):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
