from django.db import models
from django.utils.timezone import now

# Create your models here.
class query(models.Model):
    s_no=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    date=models.DateTimeField(default=now)
    content=models.TextField()
