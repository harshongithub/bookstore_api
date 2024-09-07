from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib.auth.views import LoginView, LogoutView

router = routers.DefaultRouter()
router.register(r"books",Bookviewset)

urlpatterns = [
    path('', home ,name="web_home"), 
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('api/register/', register, name='register'),
    path('api/', include(router.urls))
    
    
]