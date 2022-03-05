from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=50)
    uuid_image = models.CharField(max_length=100, default='', editable=False)
    file = models.FileField(upload_to='files/')
    create_date = models.DateTimeField(auto_now_add=True)

class User(AbstractUser):
    full_name = models.CharField(max_length=150)
    signature = models.OneToOneField(File, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)

class SignatureRequest(models.Model):
    subject = models.CharField(max_length=100)
    document = models.ForeignKey(File, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

class SignatureRequestUser(models.Model):
    request = models.ForeignKey(SignatureRequest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pos_x = models.IntegerField()
    pos_y = models.IntegerField()
    num_page = models.IntegerField()
    signed = models.BooleanField(default=False)
    signature_date = models.DateTimeField(default=None, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
