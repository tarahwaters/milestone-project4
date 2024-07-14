from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=50, blank=True, null=True)
    # Automatically set the field to 'now' when the object is first created.
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question
