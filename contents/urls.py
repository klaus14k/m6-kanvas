from django.urls import path
from contents.views import CreateContentView, RetrieveUpdateDestroyContentView

urlpatterns = [
    path("courses/<uuid:pk>/contents/", CreateContentView.as_view()), 
    path("courses/<uuid:pk>/contents/<uuid:id>/", RetrieveUpdateDestroyContentView.as_view())
]