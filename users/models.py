from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    profile_pix = models.ImageField(null=True,blank=True,upload_to='profile',default='https://static.vecteezy.com/system/resources/thumbnails/024/183/502/small/male-avatar-portrait-of-a-young-man-with-a-beard-illustration-of-male-character-in-modern-color-style-vector.jpg')
    def __str__ (self):
        return self.fullname