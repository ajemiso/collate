from rest_framework import viewsets
from .serializers import SubmittalSerializer
from .models import Submittal


class SubmittalViewSet(viewsets.ModelViewSet):

    queryset = Submittal.objects.all()
    serializer_class = SubmittalSerializer
