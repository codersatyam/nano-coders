from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class posts(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField( blank=True)
    def __str__(self):
        return self.title + '  by-  ' + self.author

class  blogcomments (models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(posts, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[:15]  + "..." + "by-" + self.user.username

class create(models.Model):
    s_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    date=models.DateField(default=now)
    slug=models.CharField(max_length=50)
    email=models.EmailField()
    content=models.TextField()