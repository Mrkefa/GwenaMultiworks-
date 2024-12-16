from django.contrib import admin
from myapp.models import Message, Comment, ImageModel, Booking
from .models import Project

# Register your models here.
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(ImageModel)
admin.site.register(Booking)


