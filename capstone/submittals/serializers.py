from rest_framework import serializers
from .models import Person, Submittal


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'
