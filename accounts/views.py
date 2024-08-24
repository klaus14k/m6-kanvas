from rest_framework import generics
from accounts.serializers import AccountSerializer

class AccountView(generics.CreateAPIView):
    serializer_class = AccountSerializer