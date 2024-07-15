from django.db import models

class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email
