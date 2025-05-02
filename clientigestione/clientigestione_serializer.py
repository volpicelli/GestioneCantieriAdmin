from rest_framework import serializers
from django.core import serializers
from home.models import ClientiGestioneCantieri


class ClientiGestioneserializer(serializers.ModelSerializer):

    class Meta:
        model = ClientiGestioneCantieri

        fields = '__all__'
