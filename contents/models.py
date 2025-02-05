from django.db import models
import uuid

class Content(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    content = models.TextField()
    video_url = models.CharField(max_length=200, null=True)

    course = models.ForeignKey("courses.Course", on_delete=models.PROTECT, related_name="contents")