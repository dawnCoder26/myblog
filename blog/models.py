from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    #if this function isnt included, a single post would be written as post object
    def __str__(self):
        return self.title

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Enquiries"

