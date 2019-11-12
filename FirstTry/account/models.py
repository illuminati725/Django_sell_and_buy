from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class UserInfo(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(null=True,max_length=10)
    date_time=models.DateTimeField(default = now, editable = False)
    profile_pic = models.ImageField(upload_to = 'profile_pics/',default='noprofile.png',blank=True)

    def __str__(self):
        return self.user.username
