from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.models import Course
from contents.models import Content
from contents.serializers import ContentSerializer
from contents.permissions import CheckStudent, isSuperUserOrReadOnly

class CreateContentView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isSuperUserOrReadOnly]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "pk"

class RetrieveUpdateDestroyContentView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CheckStudent]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "id"
    
    def get_object(self):
        try:
            Course.objects.get(pk=self.kwargs["pk"])
            content_id = Content.objects.get(pk=self.kwargs["id"])
        except Course.DoesNotExist:
            raise NotFound({"detail": "course not found."})
        except Content.DoesNotExist:
            raise NotFound({"detail": "content not found."})
        
        self.check_object_permissions(self.request, content_id)
        return content_id
