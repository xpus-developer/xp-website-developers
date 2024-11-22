from django.contrib import admin
from .models import ContactMessage
from .models import UploadedImage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')  # Display columns in the admin panel
    list_filter = ('is_read',)  # Filter messages by whether they've been read
    search_fields = ('name', 'email', 'message')  # Allow searching by name, email, or message content

admin.site.register(ContactMessage, ContactMessageAdmin)
@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

# Register your models here.
