from django.db import models

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)  # Name of the person sending the message
    email = models.EmailField(max_length=255)  # Email of the person sending the message
    message = models.TextField()  # The message content
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the time when the message is created
    is_read = models.BooleanField(default=False)  # A flag to mark if the message has been read by the admin

    def __str__(self):
        return f"Message from {self.name} at {self.created_at}"

class UploadedImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
