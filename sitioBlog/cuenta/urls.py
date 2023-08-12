from django.urls import path
from .views import RegisterView, get_user_profile
from .views import update_user_profile
#from .views import update_user_name
#from .views import update_user_credit
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/get_profile/', get_user_profile, name='get_user_profile'),
    path('user/update_profile/', update_user_profile, name='update_user_profile'),
    path('admin/', admin.site.urls),
    path('credit-card-service/', include('credit_card_microservice.urls')),
]
