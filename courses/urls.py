from django.urls import path
from courses.views import CreateReadCourseView, RetrieveUpdateDestroyCourseView, RetrieveUpdateCourseView

urlpatterns = [
    path("courses/", CreateReadCourseView.as_view()), 
    path("courses/<uuid:pk>/", RetrieveUpdateDestroyCourseView.as_view()),
    path("courses/<uuid:pk>/students/", RetrieveUpdateCourseView.as_view())
]