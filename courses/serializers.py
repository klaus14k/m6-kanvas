from rest_framework import serializers
from .models import Course
from students_courses.serializers import StudentCourseSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "status", "start_date", "end_date", "instructor", "contents", "students_courses"]
        read_only_fields = ["id", "contents", "students_courses"]

class CoursesUpdateSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        read_only_fields = ["name"]