from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class  Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('waterprojects', 'Water Projects'),
        ('assets', 'Assets'),
        ('constructions', 'Constructions'),
        ('roadworks', 'Road Works'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    user_name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=500, null=True, blank=True)
    rating = models.IntegerField( null=True, blank=True,
        validators=[
            MinValueValidator(1),  # Minimum rating is 1
            MaxValueValidator(5),  # Maximum rating is 5
        ],
        help_text="Rate between 1 and 5 stars.")

    def __str__(self):
        return self.title

from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate booking with user
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    contact_info = models.CharField(max_length=100)
    service_date = models.DateField()
    service_type = models.CharField(max_length=50)
    budget = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.service_type} for {self.name} on {self.service_date}"



