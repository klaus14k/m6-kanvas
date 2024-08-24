from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.models import Course
from courses.serializers import CourseSerializer, CoursesUpdateSerializer
from courses.permissions import IsSuperuser
from accounts.models import Account

class CreateReadCourseView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuser]
    serializer_class = CourseSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            queryset = Course.objects.filter(students = self.request.user)
        else:
            queryset = Course.objects.all()
        return queryset

class RetrieveUpdateDestroyCourseView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "pk"

class RetrieveUpdateCourseView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    queryset = Course.objects.all()
    serializer_class = CoursesUpdateSerializer
    lookup_url_kwarg = "pk"

    def update(self, request, *args, **kwargs):
        course = self.get_object()

        for item in request.data.get("students_courses"):
            student_email = item.get("student_email")
            if not student_email:
                return Response(
                    {
                        "detail": "Missing student_email"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            try:
                student = Account.objects.get(email=student_email)
            except Account.DoesNotExist:
                return Response(
                    {
                        "detail": f"No active accounts was found: email@quenaoexiste.com.br."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            course.students.add(student)
            course.save()
        
        serializer = self.get_serializer(course)
        return Response(serializer.data)
