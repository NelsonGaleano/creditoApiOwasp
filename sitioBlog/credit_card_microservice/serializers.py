# credit_card_microservice/serializers.py
#serializadores para el microservicio, hicimos esto aparte hina.

from rest_framework import serializers
from .models import CreditCard

class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['card_number', 'expiration_date', 'cvv']