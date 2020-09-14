from django.db import models
from django.contrib.auth.models import User

GENDERS = (
   ('male', 'MALE'),
   ('female', 'FEMALE'),
)

class profile(models.Model):                                               #model for the cab booker
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    gender = models.CharField(max_length=6, choices=GENDERS, default='male')
    dp = models.ImageField(default='default-pic.jpg', blank='True', upload_to = 'user_dp')

    def __str__(self):
       return self.user.username
