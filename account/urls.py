from django.urls import path
from account.views import RegisterUser, LoginUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('token/refresh/',TokenRefreshView.as_view(), name='refresh_token'),
    path('token/', TokenObtainPairView.as_view(), name='access_token')

]