from rest_framework import serializers
from .models import Person, Submittal
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)

class PersonSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Person
        fields = '__all__'


class SubmittalSerializer(serializers.ModelSerializer):

    loan_processor = PersonSerializer()

    class Meta:
        model = Submittal
        fields = '__all__'
