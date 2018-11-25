from django.contrib import admin
from .models import Post
from .models import Enquiry

# Register your models here.
admin.site.register(Post)
admin.site.register(Enquiry)