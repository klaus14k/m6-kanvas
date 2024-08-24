from django.db import models
import uuid

class STUDENT_COURSE_STATUS(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"

class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(choices=STUDENT_COURSE_STATUS.choices, default=STUDENT_COURSE_STATUS.PENDING)

    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="students_courses")
    student = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="students_courses")