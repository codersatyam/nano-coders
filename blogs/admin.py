from django.contrib import admin
from .models import posts, blogcomments, create
# Register your model(s) here.
admin.site.register((posts , blogcomments, create))
