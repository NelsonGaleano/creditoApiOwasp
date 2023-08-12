# Create your models here.
# credit_card_microservice/models.py
# este es el modelo para TARJETAS de CREDITO

from django.db import models
from django.conf import settings

class CreditCard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='credit_cards')
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return f"Card ending in {self.card_number[-4:]}"

