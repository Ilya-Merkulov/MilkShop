from django.urls.conf import path
from .views import  UserDetail, UserList

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify-token/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/users/', UserList.as_view(), name='users'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='users'),
    path('api/users/registration', UserList.as_view(), name='users/registration'),
]
