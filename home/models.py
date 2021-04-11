from django.db import models

# Create your models here.
class contact(models.Model):
    s_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=11)
    query=models.TextField()

    def __str__(self)   :
        return self.name + " -"+ self.email