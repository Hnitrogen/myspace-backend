from django.contrib import admin
from django.urls import path , include 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers
from myspace.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet,basename='users')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin', admin.site.urls),
    
    path('',include('chat.urls')),
    path('',include('account.urls')),
    path('',include('myspace.urls.index')),
]