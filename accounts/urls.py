from django.urls import path
from accounts.views import AccountView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [path("accounts/", AccountView.as_view()), path("login/", TokenObtainPairView.as_view())]