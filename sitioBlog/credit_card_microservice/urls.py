# credit_card_microservice/urls.py

from django.urls import path
from .views import CreditCardListView

urlpatterns = [
     path('credit-cards/<int:user_id>/', CreditCardListView.as_view(), name='credit-card-list'),
    # Puedes agregar más URLs aquí si necesitas más endpoints
]