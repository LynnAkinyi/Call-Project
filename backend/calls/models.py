from django.db import models

# Create your models here.
class CallLog(models.Model):
    call_type = models.CharField(max_length=50)  # Inquiry, Feedback, etc.
    phone_number = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")
