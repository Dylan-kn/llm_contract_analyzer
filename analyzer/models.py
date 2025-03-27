from django.db import models

# Create your models here.
class Contract(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='contracts/')
    raw_text = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    key_info = models.TextField(blank=True)
    red_flags = models.TextField(blank=True)

def__str__(self):
    return f"Contract {self.id} - {self.uploaded_at.date()}"

