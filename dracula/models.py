from django.db import models

# Create your models here.

# index contact us form
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, default="")
    phone = models.CharField(max_length=20, default="")
    subject = models.TextField(max_length=70, default="")
    message = models.TextField(max_length=500, default="")
    def __str__(self):
        return self.name
