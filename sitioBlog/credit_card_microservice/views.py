#vistas del microservicio para tarjeta de credio

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import CreditCard
from .serializers import CreditCardSerializer

from rest_framework.generics import ListAPIView
from .models import CreditCard
from .serializers import CreditCardSerializer

class CreditCardListView(ListAPIView):
    serializer_class = CreditCardSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = CreditCard.objects.filter(user_id=user_id)
        return queryset